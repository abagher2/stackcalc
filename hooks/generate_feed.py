"""MkDocs hook to generate an RSS 2.0 feed for the StackCalc blog."""
import email.utils
from datetime import datetime, timezone
from pathlib import Path
import re
import yaml

def on_post_build(config, **kwargs):
    site_dir = Path(config["site_dir"])
    docs_dir = Path(config["docs_dir"])
    site_url = config.get("site_url", "https://www.stackcalc.io").rstrip("/")
    blog_posts_dir = docs_dir / "blog" / "posts"

    if not blog_posts_dir.exists():
        return

    items = []
    # Find all html files in site_dir/blog/2026/*/*/index.html
    html_posts = {}
    for p in site_dir.glob("blog/[0-9][0-9][0-9][0-9]/[0-9][0-9]/[0-9][0-9]/*/index.html"):
        # relative path from site_dir
        rel = p.relative_to(site_dir).parent
        slug = rel.name
        html_posts[slug] = f"{site_url}/{rel}/"

    md_files = sorted(blog_posts_dir.glob("*.md"), reverse=True)
    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        if not content.startswith("---"):
            continue
        try:
            _, fm_text, body = content.split("---", 2)
            meta = yaml.safe_load(fm_text) or {}
        except Exception:
            continue

        title = meta.get("title", md_file.stem)
        description = meta.get("description", "")
        date_val = meta.get("date")

        # Convert date to RFC-822 format
        if isinstance(date_val, str):
            dt = datetime.fromisoformat(date_val)
        elif hasattr(date_val, "year"):
            dt = datetime(date_val.year, date_val.month, date_val.day)
        else:
            dt = datetime.now()
        dt = dt.replace(tzinfo=timezone.utc)
        pub_date = email.utils.format_datetime(dt)

        # Match corresponding HTML post URL
        post_url = None
        # Attempt match by slug in html_posts
        for slug, url in html_posts.items():
            # simple fuzzy or containment match
            clean_title = re.sub(r"[^a-zA-Z0-9]+", "-", title.lower()).strip("-")
            if slug in clean_title or clean_title in slug or slug in md_file.stem:
                post_url = url
                break
        if not post_url:
            date_prefix = dt.strftime("%Y/%m/%d")
            post_url = f"{site_url}/blog/{date_prefix}/{md_file.stem}/"

        categories = meta.get("categories", [])
        cat_xml = "".join(f"<category>{c}</category>" for c in categories)

        items.append(f"""    <item>
      <title><![CDATA[{title}]]></title>
      <link>{post_url}</link>
      <guid isPermaLink="true">{post_url}</guid>
      <pubDate>{pub_date}</pubDate>
      <description><![CDATA[{description}]]></description>
      {cat_xml}
    </item>""")

    feed_items_str = "\n".join(items)
    now_rfc822 = email.utils.format_datetime(datetime.now(timezone.utc))

    feed_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>StackCalc32 Engineering Blog</title>
    <link>{site_url}/blog/</link>
    <description>A high-quality, everyday-use RPN calculator for a new generation.</description>
    <language>en-us</language>
    <lastBuildDate>{now_rfc822}</lastBuildDate>
    <atom:link href="{site_url}/blog/feed.xml" rel="self" type="application/rss+xml" />
{feed_items_str}
  </channel>
</rss>
"""
    # Write to site/blog/feed.xml
    blog_site_dir = site_dir / "blog"
    blog_site_dir.mkdir(parents=True, exist_ok=True)
    (blog_site_dir / "feed.xml").write_text(feed_xml, encoding="utf-8")

    # Also save in docs/blog/feed.xml so it can be served or tracked
    blog_docs_dir = docs_dir / "blog"
    blog_docs_dir.mkdir(parents=True, exist_ok=True)
    (blog_docs_dir / "feed.xml").write_text(feed_xml, encoding="utf-8")

    print(f"INFO    -  Generated blog RSS feed at {blog_site_dir / 'feed.xml'} with {len(items)} items")
