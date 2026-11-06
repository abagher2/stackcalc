#!/usr/bin/env python3
"""
Unit Story Essays, Section-by-Section Character Narrative Paragraphs,
and Step-by-Step SC-6 Calculator Work-Check Guides for the StackCalc SC-6
Big Ideas Math Middle School Supplement.

Note: All curriculum planning metadata (real-world mechanisms, character roles,
and pedagogical targets) is kept strictly in Python comments below and must
never appear as banners or labels in student-facing content.
"""

from __future__ import annotations
from typing import Any, Dict

UNIT_STORIES: Dict[int, Dict[str, Any]] = {
    # =========================================================================
    # Planning Metadata — Unit 1:
    #   Real-world mechanisms: Expedition packing (remainders), pixel grids &
    #     bacterial doubling (exponents), multi-part kit pricing (PEMDAS),
    #     array layouts (prime factors), zero-waste kits & gear/bus cycles (GCF/LCM).
    #   Characters: Maya (trail-crew quartermaster), Leo (bike & robotics builder),
    #     Zoe (wildlife field tracker), Sam (skate builder).
    # =========================================================================
    1: {
        "story_title": "The Backcountry Trail Crew & Maker Cabin",
        "paragraphs": [
            "Every summer in the Cascade Mountains, a group of sixth-grade volunteers helps the ranger station prepare backcountry campsites, wildlife observation blinds, and a small maker cabin. Maya signed up to organize the supply crates and battery banks, even though she secretly worried she would mess up the counts and leave a trail crew short on gear miles from the nearest road. Across the cabin, Leo tinkers with mountain bikes, solar signboards, and LEGO robotics prototypes, while Zoe hikes with the field biologists to watch Clark's nutcrackers hide thousands of pine seeds for the winter.",
            "During their first week, guessing got all three of them into trouble. When Maya tried to pack 53 lithium battery cells into 6-cell drone packs, her phone calculator gave her a long decimal that didn't tell her how many real packs she could actually clip into a drone. When 78 campers showed up at the lake for 4-person canoes, Leo wasn't sure whether to round up or down so nobody got left on the dock. And when Sam and Leo added up the cost of a skateboard deck plus four wheels, they got two completely different totals from the exact same numbers.",
            "In the bike and robotics shed, Leo noticed another puzzle: two gears with spiky teeth only mesh smoothly when their tooth counts share common building blocks, and two park shuttles leaving the trailhead on different schedules only meet up at the station when their loop times hit a shared multiple. Even Zoe's field notes on periodical cicadas that emerge every 12 or 15 years followed the exact same pattern.",
            "None of them felt like 'math people' at the start of the summer. But by working out each supply puzzle by hand first and then checking their answers on their SC-6 calculators, they discovered that whole numbers have built-in patterns for leftovers, rapid doubling, grouping rules, and repeating cycles—turning messy real-world guesses into plans they could trust.",
        ],
    },
    # =========================================================================
    # Planning Metadata — Unit 2:
    #   Real-world mechanisms: Kitchen measuring cups (LCD fractions), recipe
    #     scaling & battery drain (multiplying fractions), crow water-displacement
    #     tubes & carpentry cuts (dividing fractions), 3D printer slicers &
    #     stopwatches (decimal operations).
    #   Characters: Elena (junior baker), Marcus (3D-printer operator), Zoe (bird lab helper).
    # =========================================================================
    2: {
        "story_title": "The Kitchen Bakery, the Avian Lab & the 3D Print Shop",
        "paragraphs": [
            "If you spend an afternoon helping Elena in her family's bakery kitchen, volunteering with Zoe at the bird-rehab aviary, or watching Marcus run the school's desktop 3D printer, you quickly run into an annoying truth: real measurements almost never land on whole numbers. Elena's measuring scoops are stamped in halves, thirds, quarters, and eighths, and she used to dread fractions because every rule felt backward—why did a bigger number on the bottom mean a smaller scoop?",
            "Next door at the wildlife center, Zoe watches New Caledonian crows bend hooked twigs to pull grubs out of logs and drop pebbles into water tubes, raising the water level by tiny fractions of a centimeter with each splash until a floating treat rises within reach. To know how many pebbles a crow needs, Zoe has to figure out how many 3/8-centimeter splashes fit inside a 4 1/2-centimeter rise.",
            "Meanwhile, in the maker room, Marcus deals with decimals every time he prints a part: the 3D printer's 'slicer' software chops a 14.4-millimeter bracket into paper-thin horizontal layers, each just 0.20 millimeters thick, and melts corn-based plastic one layer at a time. Out on the track, the stopwatch times 100-meter sprints to the hundredth of a second, where 0.55 seconds is the gap between first and second place.",
            "At first, Elena, Zoe, and Marcus all second-guessed themselves whenever fractions or decimals showed up. Across these lessons, they learn how to trade unequal fraction slices for matching pieces, why taking a 'part of a part' shrinks a fraction, how dividing fractions counts how many scoops fit inside a whole, and how to verify every fraction and decimal step on the SC-6 calculator.",
        ],
    },
    # =========================================================================
    # Planning Metadata — Unit 3:
    #   Real-world mechanisms: Bicycle front/rear sprockets (ratios), aquarium
    #     salt & bulk recipes (ratio tables), supermarket unit pricing (unit rates),
    #     battery bars & sale coupons (percents & unit conversions).
    #   Characters: Devon (bike mechanic), Priya (robotics club treasurer), Zoe.
    # =========================================================================
    3: {
        "story_title": "Bicycle Sprockets, Supermarket Aisles & Field Surveys",
        "paragraphs": [
            "Devon always wondered why pedaling his mountain bike uphill felt impossible in high gear, while shifting to low gear made his feet spin fast and easy. Flipping his bike upside down in the driveway, he counted 48 spiky teeth on the front pedal sprocket and 16 teeth on the back wheel sprocket. Because each link of the metal chain grabs one tooth at a time, pulling 48 front teeth forward forces the 16-tooth back gear to spin around three full times! One turn of Devon's feet spins the rear tire three times—trading harder pedal push for triple the speed.",
            "That same day, Priya was at the grocery store buying granola bars for the robotics club and felt stuck in front of the shelf. Box A had 6 bars for $4.50, while Box B had 10 bars for $7.00. At first she thought the $4.50 box had to be the better deal simply because $4.50 is smaller than $7.00, until she wondered if she was paying more per bar without realizing it.",
            "Over at the wildlife center, Zoe had a similar comparison problem: how do you fairly compare 17 out of 20 gigabytes used on a field tablet, 9 out of 25 penalty kicks made on the soccer field, and 21 out of 24 counting questions answered by an African grey parrot when every total is different?",
            "Whether Devon is comparing bike gears, Priya is stretching the club snack budget, or Zoe is scaling scores to a 0-to-100 percent meter, all three of them learn how ratios, unit rates, and percents let you compare almost anything fairly—and how to check every ratio, unit rate, and percent change on the SC-6.",
        ],
    },
    # =========================================================================
    # Planning Metadata — Unit 4:
    #   Real-world mechanisms: Video game scoreboards & physics formulas (variables),
    #     inventory sorting (combining like terms), team uniform bundles (distributive
    #     property), identical gift-bag packing (factoring with GCF).
    #   Characters: Noah (indie game coder), Maya (craft booth manager), Zoe.
    # =========================================================================
    4: {
        "story_title": "Coding an Arcade Game & Running the School Craft Booth",
        "paragraphs": [
            "When Noah tried to code his first arcade game for the school STEM showcase, he almost deleted the whole project in frustration. To track a player's carnival tickets, he started writing one line of code for 1 ride, another line for 2 rides, and another for 3 rides. By twenty lines, his screen was a tangled mess. And when letters like x and g showed up in his math homework that same week, he complained that letters belonged in English class, not math.",
            "Then his older sister showed him that a letter in code—and in algebra—isn't a mystery to be afraid of: it's just a labeled box that holds whatever number changes from turn to turn. Writing one short rule like 50 - 4r let the computer plug in any number of rides r and find the remaining tickets in a split second.",
            "Across the gym at the craft booth, Maya was having the same trouble keeping track of custom soccer uniform bundles—where every player needed both a jersey and $7 shorts—and packing leftover stickers into identical gift bags without coming up short.",
            "As Noah, Maya, and Zoe work through these lessons, their nervousness around letters in math fades away. They see how plugging numbers into a formula, sorting matching items into neat piles, and bundling or unbundling group orders makes their work shorter—and how substituting a test number on the SC-6 proves whether two algebraic expressions are truly equivalent.",
        ],
    },
    # =========================================================================
    # Planning Metadata — Unit 5:
    #   Real-world mechanisms: Slanted parking spaces & patio pavers (parallelograms),
    #     sailboat mainsails & skate ramps (triangles), vaulting boxes & cornhole
    #     cutouts (trapezoids & composite shapes), GPS grids & 60-minute flight clocks.
    #   Characters: Liam (skate-ramp builder), Sora (junior sailor), Zoe.
    # =========================================================================
    5: {
        "story_title": "Building Skate Ramps, Measuring Sails & Navigating by Grid",
        "paragraphs": [
            "When Liam set out to build a wooden skateboard launch ramp and a pair of cornhole boards in his garage, he hit a wall right away at the hardware store. Plywood and grip tape are sold by the square foot, yet almost none of the pieces in his sketch were plain rectangles. The side panels of his ramp were right triangles, the gym vaulting box he wanted to copy had trapezoid sides, and the cornhole board had a square hole cut right out of the middle.",
            "Down at the marina, Sora felt just as unsure when she had to order replacement sailcloth for a triangular mainsail and measure diagonal boat-trailer spaces in the lot. Whenever slanted sides and strange angles appeared, both Liam and Sora worried they would mix up which numbers to multiply and waste expensive materials.",
            "Even plotting a rectangular field on a map grid or adding flight times across the 60-minute clock mark tripped them up when they tried to count squares one by one or add minutes like ordinary base-10 decimals.",
            "Everything changed when they took a pair of scissors to scrap cardboard and saw that every parallelogram, triangle, and trapezoid is secretly built from ordinary rectangles. Once they learned to slice and slide shapes by hand—and check their areas and elapsed times using the geometry and clock keys on the SC-6—they never had to guess a formula again.",
        ],
    },
    # =========================================================================
    # Planning Metadata — Unit 6:
    #   Real-world mechanisms: Harbor ROV dives & Andean hummingbird torpor (integers),
    #     underwater depth vs. Arctic thermometers (comparing rationals), winch cables &
    #     plunging gannets (absolute value), 4-quadrant marine radar & map distances.
    #   Characters: Kai (oceanography ROV pilot), Zoe, Mia (drone mapper).
    # =========================================================================
    6: {
        "story_title": "Deep-Sea Rovers, Plunging Seabirds & Four-Quadrant Radar",
        "paragraphs": [
            "For Kai, who helps pilot a tethered underwater camera rover with the harbor oceanography club, zero isn't nothing—it's the glittering surface of the sea. High above the boat, a northern gannet circles at +32 meters in the air before folding its wings and plunging straight through the waves down to -14 meters underwater. Meanwhile, in the high Andes mountains, Zoe reads field logs about tiny hummingbirds that survive freezing nights by dropping their body temperature by 28 degrees.",
            "At first, working below zero made Kai and Mia doubt their own common sense. On a negative number line, everything seemed backward: why was -18 degrees colder than -11 degrees, yet -11 was the greater number? And when Kai winched his rover from +25 feet on the boat deck down to -140 feet in the bay, he accidentally subtracted the numbers and came up short on cable.",
            "Mia ran into the same sign traps when plotting landmarks across all four quadrants of the harbor radar screen, mixing up which way to move first and when to add versus subtract distances between coordinates.",
            "By picturing a vertical thermometer and an underwater depth line, Kai, Zoe, and Mia untangle the difference between where a number sits (its signed value) and how far you travel from zero (its absolute value)—and use the sign-change `[+/-]` and absolute-value `[|x|]` keys on the SC-6 to verify every step.",
        ],
    },
    # =========================================================================
    # Planning Metadata — Unit 7:
    #   Real-world mechanisms: Smudged receipts & filament spools (1-step equations),
    #     coaster height bars & cargo weight limits (inequalities), bike pedal-to-wheel
    #     drives vs. flat shipping fees (2-variable relationships).
    #   Characters: Maya, Leo, Devon.
    # =========================================================================
    7: {
        "story_title": "Mystery Receipts, Roller Coaster Height Bars & Bike Drives",
        "paragraphs": [
            "In most math worksheets, you are given the starting numbers and asked for the final total. In real life, Maya noticed, it almost always happens backward: you already know the final total on a smudged receipt or the remaining plastic on a 3D-printer spool, and you have to figure out what you started with. When Maya saw 12 robotics shirts billed for $168 total, or Leo saw 185.2 grams left on a spool after a 64.8-gram print, they initially tried random guess-and-check and kept getting frustrated.",
            "Other rules don't even have a single answer. At the amusement park, Leo stood beside a sign reading 'Riders must be at least 54 inches tall,' while a freight elevator plaque warned 'At most 12 passengers.' Leo always mixed up which way the < and > symbols pointed and whether the boundary number itself counted.",
            "Meanwhile, Devon wanted to write a rule connecting how many times he pedals his bike (the input x) to how many times the rear wheel spins (the output y), and see why a bike gear rule always passes through (0, 0) while a store order with a flat $7 shipping fee does not.",
            "When Maya, Leo, and Devon start picturing every equation as a balanced two-pan scale—where doing the inverse operation to both pans unwraps the unknown number—and plugging their solution back into the SC-6 to verify that both sides balance, the guesswork disappears.",
        ],
    },
    # =========================================================================
    # Planning Metadata — Unit 8:
    #   Real-world mechanisms: Emperor penguin huddles & open-top glass tanks
    #     (prism surface area), camping tents & 4-sided dice (triangular prisms &
    #     pyramids), aquarium & crow displacement volume, pizza circles & ziplines.
    #   Characters: Zoe, Liam, Marcus.
    # =========================================================================
    8: {
        "story_title": "Penguin Huddles, Camping Tents, Aquariums & Ziplines",
        "paragraphs": [
            "Why doesn't an Emperor penguin chick freeze when Antarctic winds hit -40°C? When Zoe read that penguins survive by huddling together to shrink their exposed 'surface area' while keeping their warm 'volume' the same, she admitted she always mixed those two terms up in math class. Liam had the same headache in the workshop: when he sewed nylon for a camping tent or ordered glass for an open-top fish tank, he wasn't sure when to add flat walls and when to multiply length times width times height.",
            "Marcus ran into a surprise of his own at the team pizza night. The pizzeria offered either one 16-inch pizza or two 10-inch pizzas for the same price, and almost everyone at the table assumed two 10-inch pizzas had more food simply because 10 + 10 is 20.",
            "Out on the adventure course, they also needed to find the exact length of a diagonal zipline cable stretched from the top of a 15-meter tower to an anchor 20 meters away on the ground without climbing into the air with a tape measure.",
            "By unfolding cardboard boxes and tents flat onto the table as 2D nets, packing wooden cubes into rectangular trays, and checking prism volumes, circle areas, and right-triangle diagonals on the SC-6, Zoe, Liam, and Marcus master every 3D measurement.",
        ],
    },
    # =========================================================================
    # Planning Metadata — Unit 9:
    #   Real-world mechanisms: Basketball scoring & missing test scores (the mean),
    #     skewed video-game prices (median, mode, range), forest surveys & battery
    #     life (box plots & IQR), 3D nozzle temps & crow trial consistency (MAD).
    #   Characters: Maya, Leo, Zoe.
    # =========================================================================
    9: {
        "story_title": "Basketball Stats, Outlier Prices & Bird Puzzle Trials",
        "paragraphs": [
            "When Leo looked up the prices of five video games—$20, $25, $20, $30, and a rare $105 collector's edition—and calculated the average price as $40, he thought he must have divided wrong. How could the 'average' game be more expensive than four of the five games on the shelf? Meanwhile, on the basketball court, Maya wanted an 85 average across five quizzes after scoring 80, 88, 82, and 84 on the first four, and felt stuck trying to guess what she needed on Quiz 5.",
            "Over in the bird lab, Zoe had an even subtler puzzle. Raven A and Crow B both averaged 9 seconds to unlock a puzzle box across four trials, so on paper the two birds looked identical—even though Raven A finished in a rock-steady 8, 9, 9, and 10 seconds while Crow B swung wildly between 6 and 12 seconds.",
            "And when Maya looked at a box-and-whisker plot of 60 pine trees in the forest, she initially assumed the longest whisker held the most trees—until she learned how quartiles actually split a sorted list into four equal 25% groups.",
            "At first, all the data vocabulary—mean, median, quartiles, IQR, and MAD—sounded like alphabet soup. By working out the data tables by hand first and then entering the data list with `[Σ+]` on the SC-6 to check `[x̄]`, `[MED]`, `[IQR]`, and `[MAD]`, Maya, Leo, and Zoe learn how to read any data set accurately.",
        ],
    },
    # =========================================================================
    # Planning Metadata — Unit 10:
    #   Real-world mechanisms: Arctic weather swings & trivia penalty reversals
    #     (signed rational +/- and ×/÷), go-kart admission + lap fees (2-step
    #     equations), kea parrot token jars & batting orders (probability, nPr, nCr).
    #   Characters: Kai, Leo, Zoe, Maya.
    # =========================================================================
    10: {
        "story_title": "Arctic Weather Swings, Go-Kart Tracks & Token Jars (Grade 7 Bridge)",
        "paragraphs": [
            "As the summer wraps up, Kai, Leo, Zoe, and Maya run into challenges where two rules happen at the same time. During a camp trivia night, Kai's team was sitting at -15 points when the judge canceled a -25-point penalty, and nobody at the table could agree whether their score went up to +10 or dropped to -40. At the go-kart track, Leo had $38 to spend when admission cost $8 plus $6 per lap, and he wasn't sure which number to undo first.",
            "In the bird-cognition lab, Zoe watched video from New Zealand showing wild kea parrots peering into clear jars filled with black reward tokens and white non-reward tokens. Before a lid was even opened, the parrots chose the jar with the better fraction of black tokens—while Maya tried to figure out why picking a 1st-2nd-3rd batting order gave six times as many possibilities as picking a 3-person cleanup crew.",
            "Each of these puzzles combines multiple steps—signed numbers with fractions, multiplication with addition in a two-step equation, or counting outcomes where order does or does not matter.",
            "Step by step, the four friends discover that subtracting a negative penalty, unwrapping a two-step equation in reverse order, and comparing permutations (`[nPr]`) with combinations (`[nCr]`) follow clear, logical patterns—and they use their SC-6 calculators to verify every result on their way into seventh-grade math.",
        ],
    },
}

UNIT_HOW_THINGS_WORK_ESSAYS = UNIT_STORIES


# =============================================================================
# SECTION_STORY_PARAGRAPHS (All 45 Sections, 1.1 – 10.4)
# Placed inside each individual section right before the word problems, showing
# how the characters initially feel unsure or doubt themselves and then realize
# how the section's concepts help them solve their real-world problems.
# =============================================================================
SECTION_STORY_PARAGRAPHS: Dict[str, str] = {
    # UNIT 1
    # Planning Metadata — Sec 1.1: Expedition packing, battery banks & canoes | Character: Maya
    "1.1": (
        "At the ranger station, Maya stared at a bin of 53 lithium battery cells and felt her stomach sink. "
        "Each drone pack needed 6 cells, and when she typed 53 ÷ 6 into a phone calculator, it spat out 8.8333333—which "
        "made no sense at all when you are holding real metal batteries that cannot be cut into pieces. For a moment she "
        "worried she wasn't cut out to be supply quartermaster. Then she tried lining the batteries up in rows of 6 on "
        "the workbench and realized the messy decimal was hiding a simple whole-number remainder: 8 full rows of 6 use "
        "48 cells, leaving 5 spare cells on the table. And when 78 campers arrived for 4-person canoes that afternoon, "
        "she saw that the same remainder meant 19 full canoes wouldn't be enough—they needed a 20th canoe so the last 2 campers wouldn't be left behind."
    ),
    # Planning Metadata — Sec 1.2: Pixel grids, cubic storage & bacterial doubling | Character: Leo
    "1.2": (
        "Leo was ready to give up when his biology lab sheet asked how many bacteria there would be after a single cell "
        "split in two every hour for 6 hours. He started drawing tiny branching lines on scratch paper, lost count around "
        "thirty, and muttered that he always messed up big numbers. Sitting next to him, Maya pointed out that every hour "
        "just multiplied the count by 2 again—just like his 8-by-8 LED matrix multiplied 8 × 8 for a square and his 6-by-6-by-6 "
        "storage crate multiplied 6 × 6 × 6 for a cube. Once Leo saw that an exponent simply counts how many times a number "
        "multiplies by itself (2⁶ = 64), a whole page of messy scribbles shrank into one step he could actually trust."
    ),
    # Planning Metadata — Sec 1.3: Skateboard part lists & group ticket orders | Character: Sam & Leo
    "1.3": (
        "Sam and Leo both worked out the price of a $45 skateboard deck plus 4 wheels at $7 each, but Sam got $343 while "
        "Leo got $73. Sam was ready to crumple up his paper, convinced that math rules like PEMDAS were just made up to trick "
        "kids who aren't fast at arithmetic. Then Leo set the actual parts on the counter: one wooden deck and a plastic "
        "pack of four $7 wheels. Looking at the table, Sam suddenly saw what had happened—when he added 45 + 4 first and "
        "multiplied by 7, he was pretending he bought 49 items at $7 each! Calculating the 4-wheel bundle (4 × $7 = $28) "
        "before adding the $45 deck wasn't a random school rule after all; it matched how the parts really sit on the workbench."
    ),
    # Planning Metadata — Sec 1.4: Solar panel arrays & factor trees | Character: Maya
    "1.4": (
        "When Maya tried to arrange 48 small solar cells into a neat rectangle on the cabin roof, she kept losing track of "
        "which row widths worked evenly and which ones left awkward gaps, while a spare batch of 37 cells wouldn't form any "
        "rectangle at all except one long, skinny line. She doubted she could ever find every possible layout without guessing "
        "all afternoon. Then Leo showed her how to branch 48 down a factor tree until only prime numbers (2 × 2 × 2 × 2 × 3) "
        "remained at the tips. Even when Maya started her tree with 6 × 8 and Leo started with 4 × 12, both trees ended at "
        "the exact same prime building blocks—giving her a foolproof way to see every factor pair inside a number."
    ),
    # Planning Metadata — Sec 1.5: First-aid kits (GCF) vs. bus & gear cycles (LCM) | Character: Leo
    "1.5": (
        "Leo used to dread word problems with GCF and LCM because the two three-letter names sounded almost identical, and he "
        "always guessed the wrong one on quizzes. While helping pack 28 bandages and 42 antiseptic wipes into identical trail "
        "first-aid kits, he paused and asked himself what the physical objects were actually doing. Splitting supplies into "
        "smaller equal bags with zero leftovers meant dividing IN to find the biggest shared building block—the Greatest Common "
        "Factor (14 kits). Later, watching two camp shuttles on 18-minute and 24-minute loops and two meshing 14-tooth and "
        "21-tooth LEGO gears, he realized repeating cycles build UP into the future until they meet at the Least Common Multiple."
    ),

    # UNIT 2
    # Planning Metadata — Sec 2.1: Smoothie measuring cups & crow twig tools | Character: Elena
    "2.1": (
        "In the bakery kitchen, Elena poured 3/8 cup of blueberries and 1/4 cup of strawberries into a blender and froze when "
        "she tried to write down the total. Part of her wanted to just add across the top and bottom to get 4/12, even though "
        "she had a nagging feeling that wasn't right—how could adding berries together give her less than she started with? "
        "Picking up the clear glass measuring cup, she looked closely at the etched lines and noticed that every 1/4-cup mark "
        "was the exact same height as two 1/8-cup marks. Once she traded 1/4 for 2/8 so all the scoops were the same size "
        "(eighths), adding 3/8 + 2/8 = 5/8 cup finally made complete sense."
    ),
    # Planning Metadata — Sec 2.2: Recipe batch scaling & battery drain | Character: Elena
    "2.2": (
        "Elena always assumed multiplying had to make a number get bigger, so when her phone battery was at 4/5 charge and "
        "a game used 1/2 of that charge, she was sure she needed to divide—and got a bigger number that made no sense. "
        "Discouraged, she sketched a bar split into fifths, shaded 4 of them, and sliced that shaded part in half. Seeing only "
        "2/5 of the whole bar left, she realized that taking a 'fraction of a fraction' shrinks the piece because you are "
        "taking part of a part. Better yet, when scaling a 1 3/4-cup pancake recipe by 2 1/2 batches, dividing out matching "
        "factors on the diagonal kept the numbers small enough to multiply without getting lost."
    ),
    # Planning Metadata — Sec 2.3: Crow water-displacement tubes & carpentry cuts | Character: Zoe
    "2.3": (
        "Whenever a teacher said 'keep, change, flip' for dividing fractions, Zoe followed the steps like a robot but secretly "
        "hated that she had no idea why flipping the second fraction worked. At the bird-rehab center, she watched a crow drop "
        "pebbles into a clear tube where each pebble pushed the water up by 3/8 centimeter until the water rose 4 1/2 centimeters. "
        "She asked herself a simpler question first: how many 3/8-cm splashes does it take to raise the water 1 full centimeter? "
        "Since 1 centimeter is 8/8, it takes 8/3 pebbles per centimeter—which is the flipped fraction (the reciprocal)! Multiplying "
        "4 1/2 centimeters by 8/3 pebbles per centimeter gave 12 pebbles, and for the first time the flip rule wasn't magic anymore."
    ),
    # Planning Metadata — Sec 2.4: 3D filament weights & stopwatch sprints | Character: Marcus
    "2.4": (
        "Marcus used to panic when decimal problems had uneven lengths, like adding a 345-mm base plate, a 0.6-mm spacer, "
        "and a 0.07-mm feeler shim, because he wasn't sure whether to line up the right-hand digits or the decimal points. "
        "And when multiplying 3.25 pounds of apples by $2.40 per pound, the decimal alignment rules seemed to change completely! "
        "After accidentally getting $780 for a bag of apples, he realized he could use common-sense estimation as a safety net: "
        "when adding or subtracting, lining up the decimal points keeps tenths with tenths; when multiplying, about 3 pounds at "
        "$2.40 HAS to be near $7.80, and counting the total decimal places lands the point in that exact spot."
    ),
    # Planning Metadata — Sec 2.5: 3D-print layer slicers & coin stacks | Character: Marcus
    "2.5": (
        "Looking at the 3D-printer screen, Marcus needed to find how many 0.20-millimeter plastic layers it would take to build "
        "a 14.4-millimeter tall bracket, and how many 1.75-millimeter quarters were in a 28-millimeter stack. Long division was "
        "hard enough with whole numbers; dividing by 1.75 made him want to close his notebook. Then he thought about changing "
        "millimeters into hundredths of a millimeter: multiplying both 28 and 1.75 by 100 slid both decimal points two places right, "
        "turning 28 ÷ 1.75 into 2,800 ÷ 175. Because both numbers scaled by the same factor, the answer (16 quarters) stayed "
        "identical—and the scary decimal divisor disappeared."
    ),

    # UNIT 3
    # Planning Metadata — Sec 3.1: Bike sprockets & equal-box tape diagrams | Character: Devon
    "3.1": (
        "When a smoothie recipe called for strawberries and bananas in a 4:3 ratio using 28 pieces of fruit in all, Devon "
        "initially tried dividing 28 by 4 and 28 by 3—and when 28 ÷ 3 didn't even come out whole, he thought the problem was "
        "broken. Then he looked at the A1..A6 and B1..B5 sockets on his Prime Factor Studio lid, reserving 4 Back-Row sockets "
        "(A1..A4) for strawberries and 3 Front-Row sockets (B1..B3) for bananas. Looking at the lid, he saw his mistake right "
        "away: there were 4 + 3 = 7 equal sockets sharing the 28 fruits ([2][2][7])! Placing a [2][2] = 4 prime tower in each "
        "of the 7 sockets gave 16 strawberries and 12 bananas without any guesswork."
    ),
    # Planning Metadata — Sec 3.2: Aquarium salt mixes & pizza dough scaling | Character: Priya
    "3.2": (
        "Priya had to bake 10 pizza crusts for the robotics club using a recipe written for 4 crusts (6 cups of flour for 4 crusts), "
        "and she got stuck because 4 doesn't multiply evenly into 10. Then she built 4 = [2][2] in socket A1 and 6 = [2][3] in "
        "socket B1 of her Prime Factor Ratio Table lid and realized nobody forces you to jump from 4 to 10 in one step: she could "
        "remove the shared [2] block first (dividing by 2) in Column 2 (A2 = [2] = 2 crusts, B2 = [3] = 3 cups of flour), and then "
        "stack a [5] block onto both in Column 3 to reach A3 = [2][5] = 10 crusts and B3 = [3][5] = 15 cups of flour."
    ),
    # Planning Metadata — Sec 3.3: Grocery unit price tags & foraging speeds | Character: Priya & Devon
    "3.3": (
        "Standing in the snack aisle, Priya held a 6-bar box of granola bars priced at $4.50 and a 10-bar box priced at $7.00. "
        "Her first instinct was to grab the $4.50 box because the price tag looked smaller, while Devon guessed the 10-bar box "
        "because bulk boxes are usually cheaper—neither of them was actually sure. Instead of arguing, Priya divided the cost "
        "by the number of bars to find the price of 1 single bar: $4.50 ÷ 6 = $0.75 per bar versus $7.00 ÷ 10 = $0.70 per bar. "
        "Stripping both packages down to a 'per 1' unit rate settled the question in seconds."
    ),
    # Planning Metadata — Sec 3.4: Tablet storage bars & Alex the parrot counting trials | Character: Zoe
    "3.4": (
        "Zoe was trying to compare three different results—17 out of 20 gigabytes used on a tablet, 9 out of 25 soccer penalty "
        "kicks made, and 21 out of 24 counting trials answered by Alex the African grey parrot—and felt overwhelmed because "
        "every fraction had a different denominator. Finding a common denominator for 20, 25, and 24 looked miserable. Then she "
        "remembered that 'percent' simply means 'out of 100.' By turning each score into a percent on the same 0-to-100 scale "
        "(85%, 36%, and 87.5%), she could compare all three at a single glance."
    ),
    # Planning Metadata — Sec 3.5: Stacked sale coupons & unit conversions | Character: Priya
    "3.5": (
        "When a $100 bike helmet bundle went on sale for 20% off and Priya had an extra coupon for '10% off the sale price,' "
        "she confidently added 20% + 10% = 30% off and expected to pay $70. When the register rang up $72 instead, she thought "
        "the store had overcharged her! Writing out the two steps on paper, she saw why: the first 20% off dropped the $100 "
        "price to $80, and the extra 10% coupon came off that new $80 sale price (10% of $80 is $8, leaving $72). She realized "
        "you always have to ask what starting 'whole' a percent is being taken from."
    ),

    # UNIT 4
    # Planning Metadata — Sec 4.1: Bowling tabs, gravity drops & kea puzzle scores | Character: Noah
    "4.1": (
        "Noah used to freeze up whenever letters showed up inside math expressions like 6 + 5g or 16t², convinced that algebra "
        "was way over his head. While coding the checkout screen for a bowling game ($6 shoe rental plus $5 per game g), he "
        "realized that the letter g wasn't a number he had to solve for—it was just an empty input box waiting for the player "
        "to type how many games they bowled! Once he drew parentheses around the slot—6 + 5( )—and dropped the number 4 inside, "
        "it turned right back into ordinary arithmetic he already knew how to do."
    ),
    # Planning Metadata — Sec 4.2: Token pouches & perimeter frames (like terms) | Character: Noah
    "4.2": (
        "Looking at the expression 6x + 9 - 2x + 5, Noah was tempted to mash everything together into 18x so there would only "
        "be one piece left. To check if that made sense, he set 6 sealed pouches of x tokens and 9 loose tokens on his desk, "
        "took away 2 pouches, and added 5 loose tokens. Immediately he laughed at his first guess: you can't dump loose single "
        "tokens into the pouch count! Sorting the pouches together (6x - 2x = 4x) and the loose tokens together (9 + 5 = 14) "
        "showed him why only 'like terms' can be combined into 4x + 14."
    ),
    # Planning Metadata — Sec 4.3: Team uniform bundles & mental-math cashiers | Character: Maya
    "4.3": (
        "When Maya wrote 4(x + 7) for four soccer players each ordering an $x jersey and $7 shorts, she accidentally simplified "
        "it to 4x + 7—and couldn't figure out why her budget came up $21 short. Laying out four separate order cards on the "
        "craft booth table, she saw her mistake right away: all four players got the $x jersey AND all four players got the "
        "$7 shorts (4x + 28), whereas 4x + 7 only bought shorts for one kid! Better yet, she realized the same Distributive "
        "Property let her multiply 8 × $53 in her head without scratch paper by splitting $53 into 8($50 + $3) = $400 + $24 = $424."
    ),
    # Planning Metadata — Sec 4.4: Packing identical gift bags (factoring with GCF) | Character: Maya
    "4.4": (
        "At the end of the craft fair, Maya had (16x + 24) stickers to pack into the greatest possible number of identical "
        "gift bags, and the word 'factor the expression' on her worksheet sounded intimidating. Then she noticed that packing "
        "identical bags was just the uniform-bundle problem from the day before running in reverse! Instead of multiplying the "
        "number of bags into the parentheses, she pulled out the Greatest Common Factor of 16 and 24 (which is 8) to write "
        "8(2x + 3)—showing 8 identical gift bags with (2x + 3) stickers inside each bag."
    ),

    # UNIT 5
    # Planning Metadata — Sec 5.1: Slanted parking spaces & patio pavers | Character: Liam
    "5.1": (
        "When Liam measured a slanted parallelogram parking space in the marina lot, his tape measure showed a 10-foot base, "
        "an 18-foot straight-up perpendicular height, and a 20-foot slanted side stripe. Having three numbers confused him, "
        "and he multiplied 10 × 20 first because those were the outer edges. Unsure if 200 square feet was right, he sketched "
        "the parallelogram on grid paper, snipped off the slanted right triangle on one end, and slid it to the other end. "
        "It locked into a 10-by-18 rectangle (180 square feet)! That one cut showed him why area always uses perpendicular "
        "height, while the 20-foot slanted edge is only used when walking the perimeter."
    ),
    # Planning Metadata — Sec 5.2: Sailboat mainsails & skate launch ramps | Character: Sora & Liam
    "5.2": (
        "Sora always forgot to divide by 2 when finding the area of a triangle, especially when she was in a hurry measuring "
        "a 12-foot by 25-foot sailboat mainsail. While helping Liam cut two triangular side panels for his skate ramp out of "
        "a single rectangular sheet of plywood, she watched him draw one diagonal line from corner to corner across the rectangle. "
        "Seeing the two identical right triangles nested inside the rectangle made it impossible to forget: two matching triangles "
        "always make one rectangle or parallelogram of area b × h, so a single triangle is always half (½bh)."
    ),
    # Planning Metadata — Sec 5.3: Gym vaulting boxes & cornhole board cutouts | Character: Liam
    "5.3": (
        "The trapezoid area formula—A = ½h(b₁ + b₂)—looked so crowded with subscripts and parentheses that Liam was convinced "
        "he would never remember it on a test. Looking at the trapezoid side of a gym vaulting box (16 inches wide at the top "
        "and 28 inches wide at the bottom), he wondered what would happen if he just found the halfway average of the top and "
        "bottom widths: halfway between 16 and 28 is 22 inches. Multiplying that 22-inch average width by the 20-inch height "
        "gave 440 square inches—and he realized that 'average the two parallel bases, then multiply by the height' is the exact "
        "same formula in plain English!"
    ),
    # Planning Metadata — Sec 5.4: GPS coordinate grids & 60-minute flight timers | Character: Sora
    "5.4": (
        "When Sora plotted a rectangular park with corners at (1, 2) and (11, 8) on a map grid, she started counting little "
        "grid squares one by one and kept losing her place. And when she tried to add a 3-hour 40-minute flight to an 8:35 AM "
        "takeoff using regular base-10 column addition, she got a weird time like '11:75 AM.' Taking a breath, she realized "
        "she could subtract coordinates (11 - 1 = 10 wide and 8 - 2 = 6 tall) instead of counting squares—and on a clock, "
        "every 60 minutes bundles into 1 full hour, turning 75 minutes into 1 hour and 15 minutes (12:15 PM)."
    ),

    # UNIT 6
    # Planning Metadata — Sec 6.1: Submarine dives & hummingbird torpor | Character: Kai
    "6.1": (
        "At first, Kai felt silly writing negative signs in front of numbers—how could you have less than nothing? Then he "
        "spent Saturday on the oceanography club boat watching the depth finder. With the water's surface marked as 0 feet, "
        "a gull hovering 15 feet in the air was at +15, while the camera rover 15 feet underwater was at -15. He realized "
        "that negative numbers aren't about holding 'less than nothing' in your hand; they simply tell you which direction "
        "you moved from a starting baseline like sea level or 0°C, and every number has a mirror-image opposite the same distance from 0."
    ),
    # Planning Metadata — Sec 6.2: Arctic thermometers & seabird dive depths | Character: Zoe
    "6.2": (
        "Zoe got tripped up comparing a puffin diving to -45.8 meters and a cormorant diving to -45.25 meters. Because 45.8 "
        "is bigger than 45.25 on the positive side of zero, she initially wrote that -45.8 > -45.25—and felt frustrated when "
        "it was marked wrong. Sketching a vertical depth line down into the water cleared up her confusion: going from 0 down "
        "through -45.25 to -45.80 means -45.80 is lower (deeper and colder), while -45.25 is higher (closer to the surface, "
        "so it is the greater number). Adding a trailing zero (-45.80 vs. -45.25) made comparing negative decimals way easier."
    ),
    # Planning Metadata — Sec 6.3: Plunging gannets & winch cables (absolute value) | Character: Kai & Zoe
    "6.3": (
        "When a northern gannet plunged from +32 meters in the air down to -14 meters underwater, Kai subtracted 32 - 14 and "
        "said the bird traveled 18 meters. Looking at the photo on the screen, though, he knew that couldn't be right—the bird "
        "fell 32 meters just to hit the waves, plus another 14 meters underwater! He realized that physical distance on a tape "
        "measure or winch cable is always positive. Using absolute value to add the distance to zero plus the distance past "
        "zero (|32| + |-14| = 32 + 14 = 46 meters) kept the negative sign from tricking him."
    ),
    # Planning Metadata — Sec 6.4: 4-quadrant marine radar & lake reflections | Character: Mia
    "6.4": (
        "Whenever Mia plotted points like (-4, 3) on a four-quadrant grid, she second-guessed whether to move up-and-down "
        "first or left-and-right first, and she tried to memorize rules for reflecting points across the x-axis and y-axis "
        "that she immediately mixed up. Then Kai told her how he remembers it on the boat radar: you walk across the deck "
        "horizontally (x) before you climb or dive vertically (y). And instead of memorizing reflection rules, folding her "
        "graph paper along the horizontal x-axis showed her that a mountain peak at (8, 12) reflects straight down into the "
        "lake at (8, -12)—keeping x the same and flipping y!"
    ),
    # Planning Metadata — Sec 6.5: Harbor bridge lengths & grid polygons | Character: Mia
    "6.5": (
        "On a harbor coordinate map, Mia needed the length of a suspension bridge stretching from (-8, 5) to (11, 5), and "
        "the distance between the school gym at (-14, 6) and the library at (-5, 6). At first she didn't know when to add "
        "and when to subtract the absolute values. Plotting both pairs on a simple horizontal line, she saw why you don't "
        "need a memorized rule: the bridge crosses right over the y-axis (0), so you add the 8 units on the left plus the "
        "11 units on the right (19 units); the gym and library sit on the same side of 0, so you subtract their distances (14 - 5 = 9 units)."
    ),

    # UNIT 7
    # Planning Metadata — Sec 7.1: Concert ticket receipts & balanced scales | Character: Maya
    "7.1": (
        "Maya used to read an equals sign (=) as 'and the answer is,' which made equations with variables on the left like "
        "15t + 5 = 65 feel backward and confusing. When she looked at her $65 receipt for concert tickets ($15 per ticket t "
        "plus a $5 order fee), she realized the equals sign actually works like the center pivot of a balanced two-pan scale: "
        "the expression 15t + 5 on the left weighs the exact same as $65 on the right. And to check if t = 4 tickets is right, "
        "she didn't have to guess—she could plug 4 in (15 × 4 + 5 = 65) and see both sides balance."
    ),
    # Planning Metadata — Sec 7.2: Filament spools & altimeters (+ / - equations) | Character: Leo
    "7.2": (
        "When Leo saw the equation f - 64.8 = 185.2 for his 3D-printer spool (after a print used 64.8 grams of filament and "
        "left 185.2 grams on the scale), his knee-jerk reaction was to subtract 185.2 - 64.8 because he saw a minus sign in "
        "the problem. Looking at his answer of 120.4 grams, he stopped—how could the spool start with LESS plastic than was "
        "still sitting on the scale?! Picturing the print job like a video playing in reverse, he realized that to undo "
        "taking 64.8 grams away, you have to add the 64.8 grams back to both sides (185.2 + 64.8 = 250.0 grams)."
    ),
    # Planning Metadata — Sec 7.3: Team shirt orders & sale prices (× / ÷ equations) | Character: Maya
    "7.3": (
        "Maya knew that 12 identical robotics shirts cost $168 (12s = 168), which meant dividing both sides by 12 to find "
        "$14 per shirt. But when she hit a fraction equation—a bike on sale for 5/6 of its original price costs $150, or "
        "(5/6)p = 150—she froze. Dividing by a fraction inside an equation looked scary until she connected it to what she "
        "learned in Unit 2: if 5 fifths of the price is $150, then 1 fifth is $150 ÷ 5 = $30, and all 6 sixths (the full "
        "price) is 6 × $30 = $180! Multiplying both sides by the reciprocal (6/5) did both steps at once."
    ),
    # Planning Metadata — Sec 7.4: Coaster height bars & elevator weight limits | Character: Leo
    "7.4": (
        "Standing by the roller coaster entrance ('Riders must be at least 54 inches tall') and the freight elevator ('At most "
        "12 passengers'), Leo admitted he always mixed up 'at least' and 'at most' because the word 'least' made him think of "
        "the < sign! Then he tested his own height against the 54-inch bar: 'at least 54 inches' means 54 inches is the lowest "
        "height allowed, so you must be 54 inches OR TALLER (h ≥ 54). Asking 'Am I allowed to be EQUAL to 54?' also told him "
        "when to color in a solid dot (≥ or ≤) versus leaving an open circle (> or <) on the number line."
    ),
    # Planning Metadata — Sec 7.5: Bike high gears vs. flat shipping fees | Character: Devon
    "7.5": (
        "Devon always mixed up which variable was 'independent' and which was 'dependent,' and couldn't tell when a table "
        "followed a multiplying rule (y = kx) versus an adding rule (y = x + b). Looking at his bike, he asked a simple "
        "cause-and-effect question: do my feet make the back wheel spin, or does the back wheel force my feet to move? "
        "Since his pedal turns (x) come first and cause the wheel turns (y = 3.5x), x is independent and y depends on x. "
        "And testing x = 0 gave him an instant shortcut: 0 pedal turns means 0 wheel turns (0, 0), whereas an order with a "
        "$7 shipping fee (c = x + 7) never passes through (0, 0)!"
    ),

    # UNIT 8
    # Planning Metadata — Sec 8.1: Penguin huddles & open-top glass fish tanks | Character: Zoe & Liam
    "8.1": (
        "Liam used to plug numbers blindly into the 6-wall box formula SA = 2(lw + lh + wh) without thinking about the actual "
        "object—until he ordered too much glass for an open-top aquarium and got the wrong painted area when Zoe glued two "
        "4-centimeter wooden cubes face-to-face to model huddling penguins. When they sketched the 2D net of the fish tank "
        "flat on their blueprint, Liam saw why the formula failed him: an open-top tank only has 5 glass panels (no top lid!), and "
        "gluing two cubes together hides their 2 touching faces inside, leaving only 10 exposed outer squares instead of 12."
    ),
    # Planning Metadata — Sec 8.2: Camping tents & square-pyramid gazebo roofs | Character: Liam
    "8.2": (
        "When Liam tried to calculate the waterproof fabric needed for a triangular-prism camping tent and the shingles for "
        "a square-pyramid gazebo roof, he felt overwhelmed by all the 3D edges and slant heights. He was afraid he would count "
        "the wrong number of sides or forget to divide a triangle by 2. Then Marcus suggested mentally 'unzipping' the tent "
        "and flattening every wall onto the floor as a 2D net: 1 rectangular floor, 2 rectangular roof slopes, and 2 triangular "
        "end doors (5 faces total). Counting and labeling each flat piece in the net before doing any arithmetic kept him from missing a single wall."
    ),
    # Planning Metadata — Sec 8.3: Crow water-displacement tubes & garden beds | Character: Zoe
    "8.3": (
        "Zoe used to confuse Surface Area (square units, cm²) with Volume (cubic units, cm³) until she watched a crow drop "
        "pebbles into a rectangular water tube with an 8 cm by 5 cm base. Wrapping paper or glass goes on the flat outside "
        "walls (square centimeters), while water and pebbles fill up the 3D space inside (cubic centimeters). Even better, "
        "she saw that every rectangular prism fills up like stackable layers: one 1-centimeter-deep layer of water in the tube "
        "holds 8 × 5 = 40 cm³, so when the pebbles push 120 cm³ of water upward, dividing 120 ÷ 40 shows the water must rise "
        "exactly 3 centimeters!"
    ),
    # Planning Metadata — Sec 8.4: Pizza sizes, snow cones & zipline diagonals | Character: Marcus
    "8.4": (
        "At the team pizza party, Marcus and his friends were sure that two 10-inch diameter pizzas had more pizza than one "
        "16-inch diameter pizza—until they opened the boxes and saw how huge the 16-inch pizza really was. Working it out on "
        "a napkin, Marcus caught the two traps that fool almost everyone with circles: first, a 16-inch pizza has a diameter "
        "of 16 inches, so you MUST cut it in half to get the radius (r = 8 inches, not 16!); second, because the area formula "
        "squares the radius (A = πr²), one 8-inch radius gives 64π ≈ 201 in², easily beating two 5-inch radius pizzas (2 × 25π ≈ 157 in²)."
    ),

    # UNIT 9
    # Planning Metadata — Sec 9.1: Basketball scoring & missing test scores | Character: Maya
    "9.1": (
        "Maya scored 80, 88, 82, and 84 on her first four math quizzes and wanted a mean (average) of 85 across all five "
        "quizzes, but she felt stuck trying to guess and check different numbers for Quiz 5. Then she pictured her quiz scores "
        "as five towers of blocks that get leveled out to the exact same height of 85. For five towers to each stand 85 blocks "
        "tall, there MUST be 5 × 85 = 425 blocks in total! Since her first four quizzes already added up to 80 + 88 + 82 + 84 "
        "= 334 points, subtracting 425 - 334 = 91 told her the exact score she needed on Quiz 5 without a single guess."
    ),
    # Planning Metadata — Sec 9.2: Skewed game prices (median, mode & range) | Character: Leo
    "9.2": (
        "When Leo calculated the average price of five video games ($20, $25, $20, $30, and a rare $105 collector's edition) "
        "and got $40, he thought he had messed up the division—how could the 'average' price be higher than four of the five "
        "games?! He also admitted he sometimes forgot to put numbers in order before picking the middle number (the median). "
        "Lining the prices up from least to greatest ($20, $20, $25, $30, $105), he saw why statistics has more than one kind "
        "of average: that single $105 outlier yanked the mean up to $40, while the median ($25) sat right in the middle and "
        "told the honest truth about what a typical game costs."
    ),
    # Planning Metadata — Sec 9.3: Forest tree surveys & battery tests (box plots & IQR) | Character: Maya
    "9.3": (
        "Looking at a box-and-whisker plot of 60 pine trees (Min = 12 ft, Q₁ = 18 ft, Median = 24 ft, Q₃ = 31 ft, Max = 40 ft), "
        "Maya initially thought the longest section of the drawing held the most trees. When her coach asked how many trees "
        "were taller than 18 feet, she wasn't sure how a box plot could even tell you a headcount. Then she realized how the "
        "plot is built: ordering 60 trees and splitting them at the median, Q₁, and Q₃ chops the list into four equal groups of "
        "15 trees (25% in each section), no matter how stretched out or squished a section looks! Since three of the four "
        "quarters sit above Q₁ (18 ft), 75% of the 60 trees—45 trees—are taller than 18 feet."
    ),
    # Planning Metadata — Sec 9.4: 3D nozzle temps & raven vs. crow consistency (MAD) | Character: Zoe
    "9.4": (
        "In the bird-cognition lab, Raven A solved four puzzle trials in 8, 9, 9, and 10 seconds, while Crow B took 6, 8, 10, "
        "and 12 seconds. Both birds had the exact same mean (9 seconds), so Zoe wasn't sure how to prove mathematically that "
        "Raven A was much more consistent. When she first heard the name 'Mean Absolute Deviation (MAD),' it sounded terrifying—until "
        "she read the three words backward: first find each score's Deviation (distance) from the mean of 9, take its Absolute "
        "(positive) value so below-average and above-average distances don't cancel out, and take the Mean (average) of those "
        "distances! Raven A's average wobble was just 0.5 seconds, compared to 2.0 seconds for Crow B."
    ),

    # UNIT 10
    # Planning Metadata — Sec 10.1: Arctic temperature swings & penalty reversals | Character: Kai
    "10.1": (
        "During camp trivia night, Kai's team was sitting at -15 points when the host removed a -25-point penalty, writing "
        "-15 - (-25) on the board. Seeing two minus signs in a row made Kai's head spin, and half his team guessed their "
        "score dropped to -40. Then Kai thought about what 'removing a penalty' actually means in a game: taking away a 25-point "
        "loss is the exact same thing as giving the team +25 points! Rewriting - (-25) as + 25 turned the problem into "
        "-15 + 25 = +10 points—the same reason the vertical gap between a +4,800 m peak and a -200 m cave is 4,800 - (-200) = 5,000 m."
    ),
    # Planning Metadata — Sec 10.2: Submarine dive rates & canceled penalties | Character: Kai
    "10.2": (
        "Kai had no trouble seeing why 8 seconds of diving at -15 feet per second lands a submarine at -120 feet (8 × -15 = -120), "
        "because 8 groups of a 15-foot drop is a 120-foot drop. What bothered him was why a negative times a negative—like "
        "(-4) × (-10)—had to be positive (+40). Worse still, he sometimes mixed up adding two negatives (-4 + -10 = -14) with "
        "multiplying two negatives! Thinking of (-4) × (-10) as a referee canceling (-4) penalties of -10 points each made the "
        "difference click: combining two debts gives a deeper debt (-14), whereas removing 4 ten-point penalties boosts your score by +40."
    ),
    # Planning Metadata — Sec 10.3: Go-kart lap fees & 3D print quotes (2-step equations) | Character: Leo
    "10.3": (
        "At the go-kart track, admission was $8 plus $6 per lap r, and Leo had $38 to spend (6r + 8 = 38). At first he tried "
        "dividing 38 by 6 right away, got a messy fraction, and felt stuck. Then Maya reminded him of how you get dressed in "
        "the morning versus how you undress at night: you put your socks on first and your shoes on second, so to undo it you "
        "have to take your shoes off FIRST and your socks off SECOND! In 6r + 8 = 38, r was multiplied by $6 first and $8 was "
        "added second—so subtracting the $8 admission fee first (6r = 30) and dividing by $6 second gave a clean 5 laps."
    ),
    # Planning Metadata — Sec 10.4: Kea parrot token jars & team lineups (probability) | Character: Zoe & Maya
    "10.4": (
        "When Maya's coach needed to pick 3 players from 7 teammates, Maya couldn't understand why picking a 1st, 2nd, and "
        "3rd place batting order had 210 possibilities while picking a 3-person cleanup crew from the same 7 kids had only 35! "
        "She wrote out three players—Ali, Ben, and Cam—and suddenly saw why: in a batting order, Ali-Ben-Cam and Ben-Ali-Cam "
        "are different lineups (6 different orders for the same 3 kids!), whereas on a cleanup crew, Ali, Ben, and Cam are "
        "the exact same group of 3 people no matter whose name is called first. Dividing 210 by those 6 duplicate orders (3! = 6) "
        "explained why combinations (35) are six times smaller than permutations (210)."
    ),
}


# =============================================================================
# SC6_SECTION_CHECK_GUIDE (All 45 Sections, 1.1 – 10.4)
# Dedicated instructions for the separate "How to Check Your Work on the SC-6
# Calculator" part of every section (Practice A, Practice B, and Markdown).
# =============================================================================
SC6_SECTION_CHECK_GUIDE: Dict[str, Dict[str, str]] = {
    "1.1": {
        "check_a": "Solve 23 ÷ 4 on paper first. Then check on your SC-6: type 23 [ENTER] 4 [g][÷R]. Read the Remainder (3) on line Y and the Quotient (5) on line X! Press [f][LASTx] [×] [+] to verify 5 × 4 + 3 = 23.",
        "check_b": "Work out 135 ÷ 8 by hand first, then press 135 [ENTER] 8 [g][÷R] on your SC-6. Line X shows 16 full vans and line Y shows 7 leftover students—confirming you must round up to 17 vans! Press [f][LASTx] [×] [+] to check 16 × 8 + 7 = 135.",
    },
    "1.2": {
        "check_a": "Write out the repeated multiplication by hand first. Then check on your SC-6: press 4 [x²] to verify 4² = 16, and press 4 [x³] to verify 4³ = 64.",
        "check_b": "Calculate 3⁴ on paper first. To check any power bⁿ on your SC-6, type the base 3 [ENTER], type the exponent 4, and press [g][yˣ] to confirm 81.",
    },
    "1.3": {
        "check_a": "Follow PEMDAS on paper first. To check (8 + 4) × (9 - 3) on your SC-6, solve the first parentheses with 8 [ENTER] 4 [+] (12 waits on Y), solve the second with 9 [ENTER] 3 [-] (6 on X), and press [×] to confirm 72!",
        "check_b": "Work from the inside out on paper, then check on your SC-6 stack: type 40 [ENTER] 3 [ENTER] 2 [ENTER] 3 [+] [x²] [×] 5 [÷] [-]—the 4-line stack holds each intermediate result without parentheses keys and confirms 25!",
    },
    "1.4": {
        "check_a": "Build your factor tree for 60 by hand until every branch ends at a prime. On your SC-6, test any branch with [PRIME] (flashes YES/NO) and type 60 [g][FACT] to verify the prime factorization 2² × 3 × 5!",
        "check_b": "To check the whole number built from 2³ × 3 × 5 on your SC-6, press 2 [x³] 3 [×] 5 [×] to confirm 120 (then press [g][FACT] to see its prime factors or [f][C.FAC] to compare two numbers).",
    },
    "1.5": {
        "check_a": "Find the GCF and LCM of 20 and 50 on paper first. Then check on your SC-6: press 20 [ENTER] 50 [GCF] to confirm GCF = 10, and 20 [ENTER] 50 [f][LCM] to confirm LCM = 100 (or [f][C.FAC] for shared primes).",
        "check_b": "After solving by hand, press 18 [ENTER] 24 [GCF] on your SC-6 to verify 6 identical snack packs (and press 18 [ENTER] 24 [f][LCM] to confirm 72 when checking repeating cycles).",
    },
    "2.1": {
        "check_a": "Simplify 12/18 by hand first. On the SC-6 (like the HP-32), enter fractions with the Two-Dot [.] syntax ([.] n [.] d): type [.] 12 [.] 18 [ENTER], then press [g][SIMP] to step through common factors to 2/3!",
        "check_b": "Add 1 2/3 + 1 1/4 on paper first. On your SC-6, enter mixed numbers as w [.] n [.] d: type 1 [.] 2 [.] 3 [ENTER] 1 [.] 1 [.] 4 [+] to confirm 2 11/12 (press [f][d/c] for 35/12 or [a b/c] for mixed view).",
    },
    "2.2": {
        "check_a": "Multiply numerators and denominators (or cross-cancel) by hand first. Then check on your SC-6 using Two-Dot fraction entry: type [.] 1 [.] 2 [ENTER] [.] 3 [.] 4 [×] to verify 3/8 in simplest form.",
        "check_b": "Convert mixed numbers to improper fractions and multiply on paper first. Then check on your SC-6: type 1 [.] 1 [.] 2 [ENTER] 2 [.] 2 [.] 3 [×] to confirm 4 cups.",
    },
    "2.3": {
        "check_a": "Multiply by the reciprocal on paper first. On your SC-6, check with Two-Dot fractions: type [.] 3 [.] 4 [ENTER] [.] 1 [.] 8 [÷] (or press [f][1/x] [×] to flip 1/8 to 8/1 and multiply) to confirm 6!",
        "check_b": "Rewrite 6 3/4 ÷ 1 1/8 as improper fractions and multiply by the reciprocal by hand. Then check on your SC-6: type 6 [.] 3 [.] 4 [ENTER] 1 [.] 1 [.] 8 [÷] to verify 6 shelves.",
    },
    "2.4": {
        "check_a": "Line up the decimal points and add 14.60 + 3.85 by hand first. On your SC-6, check any place-value digit with [PV] (e.g., 14.6 [ENTER] 0.1 [PV]), then press 14.6 [ENTER] 3.85 [+] to confirm 18.45!",
        "check_b": "Multiply 3.6 × 2.25 on paper and count decimal places first. Then check on your SC-6: press 3.6 [ENTER] 2.25 [×] (and press [$] for Currency Mode or [FDISP] for fraction/decimal view) to confirm $8.10.",
    },
    "2.5": {
        "check_a": "Divide 23 ÷ 4 by hand first. On your SC-6, press 23 [ENTER] 4 [÷] and tap [FDISP], [a b/c], and [f][d/c] to cycle through 5.75, 5 3/4, and 23/4 (or use [f][0.3̄] for repeating decimals)!",
        "check_b": "Shift the decimal point 2 places right (675 ÷ 25) and divide on paper first. Then check on your SC-6: press 6.75 [ENTER] 0.25 [÷] to confirm 27 quarters, and [f][LASTx] [×] to verify 27 × 0.25 = 6.75.",
    },
    "3.1": {
        "check_a": "Model 12 to 8 with Prime Blocks ([2][2]=4 in A1..A3 and B1..B2) on paper first, then check on your SC-6: press 12 [ENTER] 8 [g][a:b] to simplify directly to 3:2 (and tap [10F] to view the Ratio Table)!",
        "check_b": "Place [2][2]=4 in the 5 + 3 = 8 tape sockets (A1..A5 and B1..B3) first, then check on your SC-6: press 32 [ENTER] 5 [ENTER] 3 [+] [÷] (4 games per socket) and 5 [×] to confirm 20 wins.",
    },
    "3.2": {
        "check_a": "Scale [3] and [2][2][2]=8 by stacking [5] on A5/B5 first, then check on your SC-6: enter 3 [ENTER] 8 [g][a:b] and press [10F] to step through the Ratio Table (or repeat steps with [g][REP]) to verify 15 to 40!",
        "check_b": "Remove shared [3] from (6, 45) and stack [5] on A3/B3 first, then check on your SC-6: press 45 [ENTER] 3 [÷] 5 [×] to confirm $75.",
    },
    "3.3": {
        "check_a": "Divide 315 words by 5 minutes on paper first to find the unit rate per 1 minute. Then check on your SC-6: press 315 [ENTER] 5 [÷] to confirm 63 words per minute.",
        "check_b": "Find both unit prices on paper first. Then check on your SC-6: press 11.60 [ENTER] 8 [÷] ($1.45 sits on Y) and 16.80 [ENTER] 12 [÷] ($1.40 sits on X), then press [g][<] (flashes YES!) to confirm $1.40 < $1.45.",
    },
    "3.4": {
        "check_a": "Convert 7/20 to a decimal and percent on paper first. Then check on your SC-6 using Two-Dot fraction entry: type [.] 7 [.] 20 [ENTER] [FDISP] to see 0.35, and press [f][▸%] (or 100 [×]) to confirm 35%.",
        "check_b": "Simplify 18/24 and scale to 100 on paper first. Then check on your SC-6: press 18 [ENTER] 24 [÷] [FDISP] to toggle between 3/4 and 0.75 (and [f][▸%] for 75%).",
    },
    "3.5": {
        "check_a": "Calculate the 25% discount on paper first. Then check on your SC-6: type 60 [ENTER] 25 [%] (which computes 25% of 60 = $15 while keeping 60 on Y!) and press [-] to get the $45 sale price.",
        "check_b": "Find the percent change and unit conversion on paper first. On your SC-6, type 250 [ENTER] 325 [g][%CHG] to verify +30%, and 32 [f][▸cm] to convert 32 inches to 81.28 cm!",
    },
    "4.1": {
        "check_a": "Substitute x = 5 into 4x + 7 on paper first. Then check on your SC-6: press 4 [ENTER] 5 [×] 7 [+] to confirm 27.",
        "check_b": "Substitute t = 5 and b = 4 into 3t² + 6b on paper first. Then check on your SC-6: press 5 [x²] 3 [×] (75 waits on Y), then 4 [ENTER] 6 [×] (24 on X), and [+] to confirm 99.",
    },
    "4.2": {
        "check_a": "Group the x-terms (4+2=6) and constants (5+3=8) on paper first. On your SC-6, test x = 2 in both forms (20 [ENTER] 6 [ENTER] 2 [×] 8 [+]) and press [≠]—it flashes NO (not unequal, proving both match!).",
        "check_b": "Combine the x²-terms, x-terms, and constants on paper first. Check each coefficient sum on your SC-6 (3 [ENTER] 2 [+] = 5x² and 5 [ENTER] 1 [-] = 4x), then test x = 2 in both expressions with [≠] (flashes NO!).",
    },
    "4.3": {
        "check_a": "Distribute 6(10 + 4) on paper first. On your SC-6, evaluate 10 [ENTER] 4 [+] 6 [×] (84 on Y) and 6 [ENTER] 10 [×] 6 [ENTER] 4 [×] [+] (84 on X), then press [≠]—it flashes NO to prove both forms are equal!",
        "check_b": "Distribute 5(2x + 3) + 4x = 14x + 15 on paper first. Check the coefficients on your SC-6 (5 [ENTER] 2 [×] 4 [+] = 14; 5 [ENTER] 3 [×] = 15) and test x = 2 in both forms with [≠] (flashes NO!).",
    },
    "4.4": {
        "check_a": "Find the GCF of 18 and 24 and factor on paper first. Check on your SC-6: press 18 [ENTER] 24 [GCF] to confirm GCF = 6, giving 6(3x + 4), and test x = 2 in both forms with [≠] (flashes NO!).",
        "check_b": "Factor 45x - 30 by hand first. Then check on your SC-6: press 45 [ENTER] 30 [GCF] to confirm GCF = 15, divide 45 ÷ 15 = 3 and 30 ÷ 15 = 2 for 15(3x - 2), and test x = 2 with [≠] (flashes NO!).",
    },
    "5.1": {
        "check_a": "Multiply base × perpendicular height (12 × 8) on paper first. Then check on your SC-6: press 12 [ENTER] 8 [f][RECT] to confirm Area = 96 cm² on X (and Perimeter = 40 cm on Y).",
        "check_b": "Solve 168 ÷ 14 by hand first to find the missing height. Then check on your SC-6: press 168 [ENTER] 14 [÷] to confirm 12 inches, and [f][LASTx] [f][RECT] to verify 12 × 14 = 168 in².",
    },
    "5.2": {
        "check_a": "Calculate ½ × 10 × 6 on paper first. Then check on your SC-6 using the Triangle Area key: press 10 [ENTER] 6 [g][TRI] (which automatically computes ½ × b × h) to confirm 30 cm²!",
        "check_b": "Double the area and divide by the base on paper first. Then check on your SC-6: press 60 [ENTER] 2 [×] 15 [÷] to confirm h = 8 in. (and test 15 [ENTER] 8 [g][TRI] = 60!).",
    },
    "5.3": {
        "check_a": "Split the shape into a rectangle and triangle on paper first. On your SC-6, clear stats with [g][CLΣ], add the rectangle (12 [ENTER] 8 [f][RECT] [Σ+]) and triangle (12 [ENTER] 5 [g][TRI] [Σ+]), and press [f][Σx] to confirm 126 ft²!",
        "check_b": "Add the parallel bases (48 + 36) and multiply by ½ × 24 on paper first. On your SC-6, press 48 [ENTER] 36 [+] 24 [g][TRI] (which takes ½ × (b₁ + b₂) × h!) to confirm 1,008 in².",
    },
    "5.4": {
        "check_a": "Subtract coordinates to find the width and height on paper first. Check on your SC-6: press 9 [ENTER] 2 [-] (7) and 8 [ENTER] 3 [-] (5), then [f][RECT] to see Area = 35 on X and Perimeter = 24 on Y!",
        "check_b": "Add the hours and minutes on paper first (rolling 60 minutes into 1 hour). Check on your SC-6 using [CLK] Planetary Clock Mode or convert H.MM values with [f][▸HR] and [g][▸HMS] to confirm 12:30 PM!",
    },
    "6.1": {
        "check_a": "Plot -15 and +15 on a number line first. On your SC-6, open [f][LINE] Number Line Mode to see signed jumps across 0, or press 15 [+/-] [ENTER] 15 [+] to confirm that opposites add to 0!",
        "check_b": "Track the deposits and withdrawals on paper first. Then check on your SC-6 (in [f][LINE] mode or standard stack): press 35 [ENTER] 50 [+/-] [+] 20 [+] to confirm a final balance of +$5.",
    },
    "6.2": {
        "check_a": "Plot -5 and -18 on a number line first. Then check on your SC-6 (in [f][LINE] mode or comparison test): type 18 [+/-] [ENTER] 5 [+/-] [f][>]—it compares X (-5) > Y (-18) and flashes YES to confirm -5 > -18!",
        "check_b": "Convert -4/5 to -0.80 and compare with -0.75 on paper first. On your SC-6, load Y with 0.75 [+/-] [ENTER], enter X as [.] 4 [.] 5 [+/-] [FDISP] (-0.8), and press [g][<]—it flashes YES to confirm -4/5 < -0.75!",
    },
    "6.3": {
        "check_a": "Find the distance from 0 on paper first. On your SC-6, view the distance on [f][LINE] Number Line Mode or press 14 [+/-] [g][|x|] to confirm |-14| = 14.",
        "check_b": "Add the distances to and past sea level on paper first. Check on your SC-6: for 50 - |-18|, press 50 [ENTER] 18 [+/-] [g][|x|] [-] to confirm 32.",
    },
    "6.4": {
        "check_a": "Check the signs of (x, y) on paper first to name each quadrant. On your SC-6, load (-6, 5) with 6 [+/-] [ENTER] 5 so Y holds x = -6 and X holds y = 5.",
        "check_b": "Reflect (-5, -8) across the y-axis on paper first (flip x, keep y). On your SC-6, press 5 [+/-] [ENTER] 8 [+/-], then swap to x with [x⇄y], flip its sign with [+/-], and swap back to see (5, -8)!",
    },
    "6.5": {
        "check_a": "Sketch the points on a grid line first to see if they cross an axis. Then check the distance between (-6, 4) and (9, 4) on your SC-6 (or in [f][LINE] mode): press 6 [+/-] [ENTER] 9 [-] [g][|x|] to confirm 15 units!",
        "check_b": "Find the horizontal width |-4 - 5| = 9 and vertical height |6 - (-2)| = 8 on paper first. Check on your SC-6: press 9 [ENTER] 8 [f][RECT] to verify Area = 72 on X and Perimeter = 34 on Y!",
    },
    "7.1": {
        "check_a": "Test x = 9 in 4x + 5 = 41 on paper first. Then use the SC-6 Equality Test: load target 41 [ENTER], evaluate 4 [ENTER] 9 [×] 5 [+], and press [≠]—it flashes NO (zero difference: Left = Right = 41)!",
        "check_b": "Write n - 8 = 25 and solve for n = 33 on paper first. Check with the SC-6 Equality Test: load 25 [ENTER], evaluate 33 [ENTER] 8 [-], and press [≠]—it flashes NO to confirm both sides equal 25!",
    },
    "7.2": {
        "check_a": "Undo + 28 by subtracting 28 on paper first (x = 45). Check on your SC-6: press 73 [ENTER] 28 [-] to get 45, then load 73 [ENTER] 45 [ENTER] 28 [+] [≠]—it flashes NO to prove 45 + 28 = 73!",
        "check_b": "Solve both equations by hand first. Check on your SC-6: press 34.8 [ENTER] 19.6 [+] (54.4 g) and Two-Dot fractions [.] 5 [.] 6 [ENTER] [.] 3 [.] 8 [-] (11/24), then test each in the original equation with [≠] (flashes NO!).",
    },
    "7.3": {
        "check_a": "Undo multiplication or division on paper first (x = 17, k = 101.5). Check on your SC-6: press 136 [ENTER] 8 [÷] (17), then test 136 [ENTER] 8 [ENTER] 17 [×] [≠]—it flashes NO to confirm 8(17) = 136!",
        "check_b": "Multiply both sides of (2/5)s = 16 by the reciprocal 5/2 on paper first. Check on your SC-6 with Two-Dot fractions: press 16 [ENTER] [.] 2 [.] 5 [f][1/x] [×] (40), then verify 16 [ENTER] [.] 2 [.] 5 [ENTER] 40 [×] [≠] (flashes NO!).",
    },
    "7.4": {
        "check_a": "Solve x - 7 ≥ 12 on paper first (boundary 19, test x = 20). On your SC-6, press 12 [ENTER] 7 [+] (19) 20 [f][≥]—it flashes YES for 20 ≥ 19 (and use [f][LINE] to see the boundary on the number line)!",
        "check_b": "Solve 3g + 15 ≤ 60 on paper first (g ≤ 15). Check the boundary on your SC-6: press 60 [ENTER] 15 [-] 3 [÷] (15), then test 60 [ENTER] 3 [ENTER] 15 [×] 15 [+] [g][≤]—it flashes YES (and view on [f][LINE])!",
    },
    "7.5": {
        "check_a": "Test whether y ÷ x or y - x is constant in each table on paper first. Check on your SC-6: press 14 [ENTER] 2 [÷] (7) and 35 [ENTER] 5 [÷] (7), then press [≠] (flashes NO!) to confirm a constant rate y = 7x.",
        "check_b": "Write p = 12.50h and multiply on paper first. Then check on your SC-6: press 12.50 [ENTER] 6.5 [×] to confirm $81.25.",
    },
    "8.1": {
        "check_a": "Unfold the 6-face net and find the area of each pair on paper first. On your SC-6, clear stats with [g][CLΣ], add each face pair using [f][RECT] 2 [×] [Σ+], and press [f][Σx] to confirm 158 cm²!",
        "check_b": "Calculate 6s² for the cube and the 5 panels of the open-top bin on paper first. Check on your SC-6: press 7 [x²] 6 [×] to confirm 294 in² for the cube.",
    },
    "8.2": {
        "check_a": "Add the square base (10²) and 4 triangles on paper first. Check on your SC-6: press [g][CLΣ] 10 [x²] [Σ+] 10 [ENTER] 12 [g][TRI] 4 [×] [Σ+] [f][Σx] to confirm 340 m²!",
        "check_b": "Add the 2 triangular ends and 3 rectangular sides on paper first. Check on your SC-6: press 6 [ENTER] 8 [g][TRI] 2 [×] (48 ft²) plus 6 [ENTER] 8 [+] 10 [+] 10 [f][RECT] (240 ft²) [+] to confirm 288 ft².",
    },
    "8.3": {
        "check_a": "Multiply length × width × height on paper first. Then check on your SC-6 using the Prism Volume pipeline: type 12 [ENTER] 8 [f][RECT] 5 [f][PRISM] (Base Area 96 × Height 5) to confirm 480 in³!",
        "check_b": "Find the base area B = 9 × 5 = 45 in² and divide 360 ÷ 45 on paper first. Check on your SC-6: press 360 [ENTER] 45 [÷] to confirm a depth of 8 inches.",
    },
    "8.4": {
        "check_a": "Cut the 12-inch diameter in half (r = 6) and calculate πr² and √(12² + 5²) on paper first. Check on your SC-6: press 6 [f][CIRC] to verify 113.10 in², and 12 [ENTER] 5 [g][HYP] to verify 13 ft!",
        "check_b": "Calculate V = ⅓πr²h on paper first. Then check on your SC-6 using the Cone Volume pipeline: type radius 3 [f][CIRC] height 10 [g][CONE] (Base Area × Height ÷ 3) to confirm 94.25 cm³!",
    },
    "9.1": {
        "check_a": "Add the 5 values and divide by 5 on paper first. On your SC-6, clear stats with [g][CLΣ], enter each value with [Σ+] (or view the dot plot in [FRQ] mode), and press [g][x̄] to confirm Mean = 21!",
        "check_b": "Multiply 4 tests × 90 = 360 and subtract the first 3 scores on paper first. Check on your SC-6: press 4 [ENTER] 90 [×] 86 [ENTER] 92 [+] 88 [+] [-] to confirm 94.",
    },
    "9.2": {
        "check_a": "Order the numbers from least to greatest on paper first! Then check on your SC-6: press [g][CLΣ], enter each number with [Σ+] (or [FRQ]), and press [f][MED], [g][MODE], and [RNG] to verify Median = 7.5, Mode = 7, and Range = 4!",
        "check_b": "Sort the 6 prices on paper first to see how the $90 outlier pulls the mean up. Enter all 6 prices with [Σ+] on your SC-6 and compare [g][x̄] ($29.17) against [f][MED] ($17.50)!",
    },
    "9.3": {
        "check_a": "Order the data and split into lower and upper halves on paper first. After entering the list with [Σ+] on your SC-6, press [f][MIN], [f][1Q], [f][MED], [g][3Q], [g][MAX], and [IQR] to check all 5 box-plot values and IQR = 16.5!",
        "check_b": "Remember each section of a box plot holds 25% of the data (so the middle box holds 50%). Check 50% of 40 students on your SC-6 (40 [ENTER] 50 [%]) to confirm 20 students.",
    },
    "9.4": {
        "check_a": "Make your 3-step MAD table (mean, absolute distances, average of distances) on paper first. Then check on your SC-6: press [g][CLΣ], enter each value with [Σ+], and press [g][x̄] (14) and [g][MAD] (2.4)!",
        "check_b": "Calculate the mean and average deviation on paper first. Then enter all 6 sprint times with [Σ+] on your SC-6 and press [g][x̄] (13.0 s) and [g][MAD] (0.40 s) to verify your table!",
    },
    "10.1": {
        "check_a": "Use zero-pair chips or a number line on paper first. On your SC-6, open [f][LINE] Number Line Mode (or [10F] zero-pair frame) and press 8 [+/-] [ENTER] 5 [+] to confirm -3, and 6 [+/-] [ENTER] 4 [+/-] [+] to confirm -10!",
        "check_b": "Rewrite subtraction as adding the opposite on paper first. Check on your SC-6 (in [f][LINE] mode or with Two-Dot fractions): press 10 [ENTER] 4 [+/-] [-] (+14°C) and [.] 3 [.] 4 [+/-] [ENTER] [.] 5 [.] 8 [+/-] [-] (-1/8).",
    },
    "10.2": {
        "check_a": "Apply the sign rules (same signs = +, different signs = -) on paper first. Check on your SC-6: press 6 [ENTER] 4 [+/-] [×] (-24) and 5 [+/-] [x²] (+25).",
        "check_b": "Divide (-5/6) ÷ (-5/12) on paper first (negative ÷ negative = positive). Check on your SC-6 with Two-Dot fractions: press [.] 5 [.] 6 [+/-] [ENTER] [.] 5 [.] 12 [+/-] [÷] to confirm +2 minutes.",
    },
    "10.3": {
        "check_a": "Undo + 7 first and × 3 second on paper (x = 7). Check on your SC-6: press 28 [ENTER] 7 [-] 3 [÷] (7), then run the Equality Test 28 [ENTER] 3 [ENTER] 7 [×] 7 [+] [≠]—it flashes NO to confirm 3(7) + 7 = 28!",
        "check_b": "Subtract 14 first, then divide by -3 on paper (h = 4). Check on your SC-6: press 2 [ENTER] 14 [-] 3 [+/-] [÷] (4), then test 2 [ENTER] 14 [ENTER] 3 [ENTER] 4 [×] [-] [≠]—it flashes NO to confirm 14 - 3(4) = 2!",
    },
    "10.4": {
        "check_a": "Write P(event) = favorable / total and simplify on paper first. Check on your SC-6: press [.] 4 [.] 10 [g][SIMP] to confirm 2/5, press 5 [x!] to confirm 5! = 120, and explore rolls with [DICE] or [f][1…x]!",
        "check_b": "Decide whether order matters first! Then check on your SC-6: press 10 [ENTER] 3 [g][nPr] to confirm 720 ordered podiums (permutations), and 10 [ENTER] 3 [f][nCr] to confirm 120 unordered crews (combinations)!",
    },
}
