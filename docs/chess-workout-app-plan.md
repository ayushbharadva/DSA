# Chess Workout App — Milestone 1 Plan

Status: **proposal only. Nothing is built yet.** Written 2026-10-09.

This file lives on the `claude/eager-ptolemy-bo6pht` branch of the DSA repo only.
It moves into the app's own repo in Milestone 2. Don't merge it into DSA `main`.

Contents:

1. [Repository inspection](#1-repository-inspection)
2. [Market check and honest verdict](#2-market-check-and-honest-verdict)
3. [Names](#3-names)
4. [Proposed stack](#4-proposed-stack)
5. [Architecture](#5-architecture)
6. [Milestones 2–12](#6-milestones)
7. [Risks](#7-risks)
8. [Sources](#8-sources)

---

## 1. Repository inspection

| Item | Finding |
|---|---|
| Repo | `ayushbharadva/DSA`: 5 Python files of data-structures practice (binary search, linear search, BST notes) |
| Stack | Python scripts. No React Native, no `package.json`, no Android project |
| Navigation, state, styling, tests | None |
| Chess code or chess libraries | None |
| Android config | None |
| Your other GitHub repos | None of them is this app |

**What can be reused:** nothing from this repo. The app needs its own new repo.

I tried to read one of your other React Native repos to copy your usual choices (state library, styling).
That was blocked in this environment, so the stack below uses common defaults. Override anything you normally do differently.

---

## 2. Market check and honest verdict

### Who already does this

| Product | What it offers | Overlap |
|---|---|---|
| **Duolingo Chess** | Free beginner course inside Duolingo: short lessons, puzzles, streaks, player-vs-player. On Android since Sept 2025, PvP on Android early 2026. About **7M daily chess learners** less than a year after launch (Duolingo, Q4 2025 call). Built for people new to chess. | Very high: same habit + beginner + streak idea, from the best habit app there is |
| **Chess.com** | 200M+ members (May 2025), about 1.5M paying. Free tier: a few puzzles and one lesson per day, plus a daily puzzle. | High for people who already play |
| **Lichess** | Free, ad-free, unlimited puzzles (~6M), puzzle themes | Medium: lots of puzzles, no guided daily routine |
| **Chessmate by PW** | Physics Wallah's chess vertical (Aug 2026, GM Vidit Gujrathi): live classes for kids, India | Low on product. But it owns the "ChessMate" name in India |
| **Indie daily-puzzle apps** | Daily Chess Puzzle Challenge, Chessle, Chess Puzzles!, ChessMate: Chess Puzzles & Tactics, ChessLab Puzzle ("daily chess brain workout") | High on format |
| **Near-identical indie** | "Chess Training: Proven Drills" (Google Play, Feb 2026): 5–20 minute daily sessions, 12 drill types, "cut blunders" | Very high |
| **Anti-blunder tools** | blunder.clinic (daily "don't blunder" puzzles), Blunders (iOS, AI coach on your games), Chess Blunder Trainer (Android) | High on the "stop blundering" angle |
| **AI coaches** | Noctie, Aimchess, Chesska, Chessiverse | Your Phase 4 |

### Verdict

**Build it, as a focused experiment and a learning project. Not as a big business bet.**

Why it's hard:

- The core idea (short daily chess workout + streak, for beginners) is not new. Duolingo already does it, free, at huge scale.
- A generic version will be invisible in the store. You can't out-feature or out-market Duolingo or Chess.com.
- Money is hard here. Even Chess.com converts under 1% of members to paid (about 1.5M of 200M).

Why it's still worth building:

- Cost is tiny: a $25 one-time Play Console fee plus your time. No servers.
- You are the target user (300 rapid). You'll use it daily and improve while building it.
- You'll learn the whole pipeline: product, content, testing, release.
- The content pipeline (free public-domain puzzles + engine checks) is reusable for anything you build next.

Where a small app can win: a narrower promise.

- **Recommended angle: "Stop blundering", for people who already play online and are stuck around 300–1000.**
  Duolingo's course is built for people new to the game and starts from how the pieces move.
  Reviewers who already play found its puzzles simple.
  Your "Spot the Blunder" and "What would you play?" types fit this angle exactly.
- **Later differentiator:** daily workouts built from the user's own Chess.com/Lichess games (both have public APIs).
  Others offer game review. Few turn your own mistakes into a 5-minute daily habit.

**Kill/continue checkpoint** (after the closed test in M12):
if at least ~1 in 4 testers still does workouts in their second week without you nudging them, keep going.
The average app keeps roughly 11–13% of users at day 7, so that is a meaningful bar.
If they don't come back, change the angle before adding features.

---

## 3. Names

### What went wrong with ChessMate

It was taken several times over:

- "Chessmate by PW" (Physics Wallah, Aug 2026).
- "ChessMate: Chess Puzzles & Tactics" on Google Play.
- A "Lucky Chessmate" trademark covering games and educational software (WIPO filing).

Chess puns made of common words are almost always taken. Distinctive names are safer.

### How the names were checked

- Web search for each name, including searches limited to `play.google.com` and `apps.apple.com`.
- US trademark mentions on aggregator sites (Justia, Trademarkia, uspto.report).
- **Not checked** (blocked in this environment or not searchable from here): Play Store and App Store search directly, domain registries, and the official trademark databases (USPTO, WIPO, IP India).

So "nothing found" is good evidence, not proof.

### Shortlist

| Rank | Name | Store title (Play limit: 30 chars) | Why it fits | What I found | Risk |
|---|---|---|---|---|---|
| 1 | **Rookie Reps** | Rookie Reps: Chess Workout | "Rookie" = beginner and hides "rook". "Reps" = daily workout | No app with this name on Play or App Store. No US trademark record found. No website found | "Chessreps" and "Chess Reps" (opening trainers) also use "reps". "Rookie" may feel limiting once users improve |
| 2 | **Look Twice** | Look Twice: Blunder Less | Names the exact habit that stops blunders. Fits the recommended angle | No chess app found. US marks "SAVE A LIFE, LOOK TWICE" (legal services) and "LOOK TWICE SAVE A LIFE" exist, outside software as far as found | Common phrase, so a weaker trademark and harder to find in search |
| 3 | **Chess Cardio** | Chess Cardio: 5-Min Workout | Playful. Says "short workout" instantly | No app found. No US trademark record found | "Chess" part is generic. "Cardio" may read as a fitness app |

### Rejected

| Name | Why |
|---|---|
| ChessMate | See above |
| Blunderproof | Chessmood sells a "BlunderProof" course. "Blunder Proof Method" is another chess course |
| Knightcap | Name of an old chess engine (KnightCap) |
| Pawnder | Name of a 1990s chess engine |
| Pawn Up | PawnUp.com was an online pawn shop. "Pawn" pulls pawn-shop search results |
| Quiet Move | Too close to QuietChess (2026 desktop game). Meaning is obscure to beginners |
| Chess in 5 Minutes, Daily Chess Workout | Descriptive phrases nobody can own. Use one as the subtitle, not the brand |

### Before you commit to a name (about 15 minutes)

1. Search the exact name in the Play Store and App Store.
2. Check the domain (e.g. `rookiereps.com` or `rookiereps.app`) on any registrar.
3. Trademark search in Nice classes **9** (software) and **41** (education/entertainment):
   - India: [tmrsearch.ipindia.gov.in](https://tmrsearch.ipindia.gov.in): Wordmark, "Contains", then Phonetic
   - US: [tmsearch.uspto.gov](https://tmsearch.uspto.gov)
   - Global: [branddb.wipo.int](https://branddb.wipo.int)
4. Check Instagram, X and YouTube handles.
5. If all clear: buy the domain and grab the handles the same day.

Store facts that matter:

- **Google Play does not require unique titles.** The **package name** (e.g. `com.ayushbharadva.rookiereps`) is the unique ID, and it can never change after you publish.
- **Apple's App Store requires unique names.** A name is reserved when you create the app record (needs the paid Apple developer account). Only relevant if you go iOS.

---

## 4. Proposed stack

Chosen for: simple, offline, Android first, iOS later without a rewrite.

| Concern | Pick | Why | Alternatives |
|---|---|---|---|
| App framework | **Expo** + TypeScript. Latest stable today: SDK 57 (React Native 0.86). SDK 58 is in beta | Fast setup, managed Android builds, easier upgrades. Everything in the MVP runs in Expo Go (no custom native code) | Bare React Native CLI (more native config to maintain) |
| Navigation | **Expo Router** (file-based, built on React Navigation) | 4–5 screens. Default in new Expo apps | React Navigation directly |
| Chess rules | **chess.js** 1.x (TypeScript; 1.4.0 is the latest found) | Mature: legal moves, check/mate/stalemate, castling, en passant, promotion, FEN/PGN | Writing our own rules: never |
| Board | **Our own small board**: 8×8 grid of pressable squares + SVG pieces | Full control over puzzle UX. Every square is reachable by TalkBack. No extra native libraries | `react-native-chessboard` v2 (MIT, maintained). It draws on a Skia canvas, which is harder to make accessible and adds Skia to the app. Kept as a fallback |
| Piece artwork | A set licensed for commercial use: **chessnut** (Apache-2.0) or **rhosgfx** (CC0) | Many popular sets are GPL or non-commercial | cburnett and merida are GPL. california, maestro, staunty and others are non-commercial. Avoid them |
| Engine (Stockfish) | Runs **only on your computer** inside the content scripts. **Never shipped in the app** | Stockfish is GPLv3, a "share-alike" license: shipping it inside your app brings duties to publish source code, possibly your whole app's (ChessBase was sued over GPL breaches). Running it privately on your laptop brings none. Also keeps the app small and light on battery | On-device Stockfish later (Phase 4), with licensing handled deliberately |
| Content source | **Lichess puzzle database**: CC0 (public domain), ~6M rated and tagged puzzles | Free even for commercial use. Engine-generated. Has theme tags (fork, pin, mateIn1, hangingPiece…) | Hand-made positions: too slow and error-prone |
| State | **Zustand** (tiny state library) with its `persist` helper | Shares progress across screens. Built-in versioned saving | React Context + useReducer (more boilerplate for saving) |
| Storage | **AsyncStorage** behind our own `storage` module | Data is a few KB. Works in Expo Go. Swappable in one file | react-native-mmkv (faster, needs a dev build), expo-sqlite/kv-store |
| Styling | `StyleSheet` + a small theme file (colors, spacing, type) with light/dark | Four screens don't need a UI kit | NativeWind, Tamagui |
| Animation, feel | Reanimated (ships with Expo) + expo-haptics | Smooth piece moves, small feedback vibrations | — |
| Tests | Jest (`jest-expo`) + React Native Testing Library. Maestro for one end-to-end flow in M11 | Standard for Expo | Detox (heavier) |
| CI | GitHub Actions: typecheck, lint, tests | Catches broken content and logic on every push | — |
| Builds | EAS Build (Expo's cloud build service) → Android App Bundle (`.aab`) | No local Android signing setup | Local Gradle builds |
| Analytics | **None in MVP.** A `track()` function that does nothing yet | Privacy and simplicity. Adding a tool later doesn't touch screens | PostHog or Firebase later |

---

## 5. Architecture

### Layers

```text
Screens (app/)               Home · Workout · Result · Progress
   ↓ call
Workout + progress logic     pick today's 3, step through, score, streak, stats   (pure TypeScript)
   ↓ call
Chess domain (src/chess)     wraps chess.js: legal moves, apply move, check/mate, move → plain words
Content (src/content)        typed challenges + validation, loaded from a bundled JSON file
Storage (src/storage)        versioned save/load that survives corruption

Content scripts (scripts/, your computer only)
   Lichess CSV → filter → Stockfish check → explanations → content/challenges.json
```

Rules:

- Only `src/chess` imports chess.js. Screens never do.
- The board knows nothing about puzzles. It shows a position and reports "the user moved e2 to e4".
- Challenge data never lives in components.
- Logic modules are pure functions, so they are testable without a phone.

### Folder structure (new repo)

```text
app/                    # screens (Expo Router)
  _layout.tsx
  index.tsx             # Home
  workout.tsx
  result.tsx
  progress.tsx
src/
  chess/                # chess rules wrapper (the only place that imports chess.js)
  components/board/     # Board, Square, Piece, PromotionPicker
  challenges/           # TacticChallenge, ChoiceChallenge, ChallengeView, answer checking
  content/              # types, validation, loader
  workout/              # today's workout selection + step-by-step state
  progress/             # streak, stats, saved store
  storage/              # AsyncStorage wrapper, schema version, migrations
  analytics/            # track(): does nothing for now
  theme/                # colors (light/dark), spacing, typography
content/
  challenges.json       # generated, committed, bundled in the app
scripts/content/        # dev-only: import, verify, explain, bundle
docs/                   # this plan, decision records, content pipeline notes
```

### Challenge data model

Terms used below:

- **FEN**: one line of text that describes a chess position.
- **UCI**: a move written as from-square + to-square, e.g. `e2e4`, or `e7e8q` for a promotion to a queen.
- **SAN**: the human notation you see on Chess.com, e.g. `Nf3`.

```ts
type ChallengeType = 'tactic' | 'spotTheBlunder' | 'bestMove';
type Difficulty = 'beginner' | 'easy' | 'medium' | 'hard';

interface ChallengeBase {
  id: string; // stable forever, e.g. "tactic-lichess-00sHx"
  type: ChallengeType; // stats category is derived: Tactics / Blunders / Decisions
  difficulty: Difficulty;
  themes: string[]; // Lichess tags: "fork", "mateIn1", "hangingPiece"…
  fen: string; // exactly what the user sees; the user is the side to move
  prompt: string; // "White to move. Win material."
  explanation: string; // shown after answering
  source: { kind: 'lichess'; puzzleId: string; rating: number } | { kind: 'original' };
  verification: { engine: string; depth: number; checkedAt: string }; // proof from the scripts
}

interface TacticChallenge extends ChallengeBase {
  type: 'tactic';
  solution: string[]; // UCI; the user plays moves 1, 3, 5…; the app plays the replies
}

interface ChoiceChallenge extends ChallengeBase {
  type: 'spotTheBlunder' | 'bestMove';
  options: { move: string; isAnswer: boolean; feedback: string }[]; // 3 options, UCI
}

type Challenge = TacticChallenge | ChoiceChallenge;
```

Adding a new challenge type later means one new member in the union and one new component in `ChallengeView`. Screens don't change.

### Content pipeline (this is where correctness comes from)

Think of it as an answer key. Stockfish writes and double-checks the key once, on your laptop. The app only compares the user's answer to the key.

1. **Import.** Read the Lichess puzzle CSV. Keep popular, low-rated puzzles with beginner themes and short solutions.
   Lichess detail: the CSV's FEN is the position *before* the opponent's move. We apply that first move to get the position the user sees.
2. **Verify.** Run Stockfish on every candidate. Drop anything the engine disagrees with.
3. **Make all three types from the same positions:**
   - *Tactic*: the Lichess solution.
   - *Spot the Blunder*: the position *before* the opponent's mistake. Options = that mistake + 2 safe moves.
     The engine must confirm the blunder loses about 2+ pawns of value and the safe moves lose about 0.5 or less.
   - *What would you play*: options = best move + 2 plausible but clearly worse moves.
     The engine must confirm a big gap (about 1.5+ pawns).
4. **Explain.** Fill beginner-friendly templates from verified facts, e.g. "Nf6+ attacks the king and the queen at once."
   You review every explanation in the MVP set. That doubles as chess training for you.
5. **Bundle.** Write `content/challenges.json`.
6. **CI guard.** A test loads the whole bundle and checks with chess.js: every FEN is valid, the user is to move,
   every solution and option move is legal, each choice challenge has exactly one answer, ids are unique, explanations exist.
   A broken challenge can't ship.

The thresholds above are starting points. We tune them in M4–M5.

Answer checking in the app:

- **Tactic:** correct if the move equals the solution move, **or** if it gives checkmate (Lichess rule: any mating move wins).
- **Choice:** correct if the chosen option has `isAnswer: true`.

### Daily workout selection (MVP)

- Content is ordered by difficulty, then rating.
- Today's workout = the first unseen challenge of each type, in order: Tactic → Blunder → Decision.
- It is saved as `{ date, challengeIds }`, so reopening the app the same day shows the same three.
- After finishing, Home shows "Done for today ✓ New workout tomorrow."
- If content runs out: repeat the ones answered wrong first, then the oldest.
- Difficulty: the content order ramps from Beginner to Easy. Adaptive difficulty waits until after MVP.

### Streak rules

- The saved **completion history** (dates + results) is the single source of truth. Streak and stats are computed from it, so they can't drift apart.
- A "day" is the phone's local calendar date when the workout was finished.
- Last completion today or yesterday: streak continues.
  Older: streak shows 0 with "Start a new streak today" (no guilt copy). Best streak stays visible.
- Finishing twice in one day counts once.
- Date math is done on calendar dates, so daylight-saving changes can't break a streak.
- Clock moved backwards: never crash, never lower stored values.

### Persistence

- One JSON value: `{ schemaVersion: 1, completions: [...], seenChallengeIds: [...], todayWorkout?: {...} }`.
- On load: parse and validate. If corrupted: start fresh, keep the raw text under a backup key, never crash.
- Schema changes go through a `migrate(fromVersion)` function, with tests.

### Analytics events (defined now, sent nowhere yet)

`app_opened`, `workout_started`, `challenge_answered { challengeId, type, correct, msToAnswer }`, `workout_completed { score, durationMs }`.

No names, emails, device IDs or location.

### Privacy

The MVP collects nothing and needs no internet. The Play "Data safety" form can say "no data collected", as long as no analytics or crash SDK is added.
We revisit this in M12 if we add crash reporting.

---

## 6. Milestones

Every milestone ends with a runnable app and green CI.

### M2: New repo + app shell

- **Goal:** Runnable Expo app with 4 placeholder screens, theme and CI.
- **Files:** `app/_layout.tsx`, `app/index.tsx`, `app/workout.tsx`, `app/result.tsx`, `app/progress.tsx`, `src/theme/*`, `app.json`, `tsconfig.json` (strict), ESLint/Prettier config, `jest.config.js`, `.github/workflows/ci.yml`, `README.md`, `docs/decisions/0001-stack.md`.
- **Approach:** `npx create-expo-app@latest` with TypeScript. Delete sample code. Stack navigation (no tabs). Light/dark theme tokens. Placeholder package name until the name is final.
- **Tests:** Home renders. CI runs typecheck, lint and tests.
- **Done when:** The app runs on an Android phone or emulator. Home → Workout → Result → Home and Home → Progress work. Dark mode follows the system. CI is green.

### M3: Chess domain + board

- **Goal:** A board that shows any position and only allows legal moves.
- **Files:** `src/chess/{position,moves,describe,index}.ts` + tests. `src/components/board/{Board,Square,Piece,PromotionPicker}.tsx` + piece SVGs. `app/dev/board.tsx` (playground, hidden in release builds).
- **Approach:** Wrap chess.js. Tap a piece → dots on legal squares → tap a dot to move. Last-move and check highlights. Flip for Black. Promotion picker. Board fits the screen with a 16px side gutter. TalkBack labels like "e4, white knight". Drag-to-move comes in M10.
- **Tests:** Legal and illegal moves. Turn order. Check, checkmate, stalemate. Castling (both sides, blocked, through check). En passant (only right after the double step). Promotion, including underpromotion. FEN round-trip. Move → plain words ("Knight to f3"). Board: 64 squares render, an illegal tap does nothing, a legal tap reports the UCI move, the promotion picker appears.
- **Done when:** On the playground you can play a full legal game with castling, en passant and promotion, and you can't make an illegal move.

### M4: Content model + pipeline + first tactic challenge

- **Goal:** Real, engine-verified beginner puzzles playable in the app.
- **Files:** `src/content/{types,validate,load}.ts`, `content/challenges.json`, `scripts/content/{import-lichess,verify-with-stockfish,explain,build-bundle}.ts`, `src/challenges/tactic/{TacticChallenge.tsx,checkTacticMove.ts}`, `src/components/Feedback.tsx`, `docs/content-pipeline.md`.
- **Approach:** Filter Lichess puzzles (beginner rating band, popular, short). Verify with Stockfish. Template explanations + your review. About 40 tactics. In the app: user moves → checked → opponent reply plays automatically → next move or done. Wrong → kind explanation + "Show solution".
- **Tests:** Whole-bundle validation (pipeline step 6). `checkTacticMove`: right, wrong, alternative checkmate accepted, promotion. Feedback renders for right and wrong.
- **Done when:** You can solve 5 different puzzles. A wrong move explains why. CI fails if any bundled challenge is broken.

### M5: Other two challenge types + progression

- **Goal:** All 3 types work, and the app can step through a list of them.
- **Files:** `src/challenges/choice/{ChoiceChallenge.tsx,checkChoice.ts}`, `src/challenges/ChallengeView.tsx`, `scripts/content/{make-spot-the-blunder,make-best-move}.ts`, more content.
- **Approach:** Generate both types from the same verified positions (see pipeline). Options are plain-language buttons ("Knight to f3 · Nf3") with an arrow preview on the board. `ChallengeView` picks the component by `type`.
- **Tests:** `checkChoice`. Generator thresholds, using saved engine results as fixtures. Bundle checks for options (all legal, distinct, exactly one answer). Step-through logic (answer → feedback → next → done).
- **Done when:** A mixed set of 3 plays end to end with correct feedback for each type.

### M6: Daily workout flow

- **Goal:** "Today's Workout" = 3 challenges for today. Same 3 if reopened today. New 3 tomorrow.
- **Files:** `src/workout/{selectTodayWorkout,workoutReducer,useWorkout}.ts`, `src/utils/dateKey.ts`, `app/workout.tsx`.
- **Approach:** Selection rules from section 5. Progress bar 1/3 → 3/3. "Quit workout?" confirmation. Resume.
- **Tests:** New user. Partial history. All seen → repeat wrong ones first. Same day → same workout. Next day → new workout. Date keys around midnight, month and year ends, daylight saving.
- **Done when:** Install → open → Start → 3 challenges → finish, with no account or setup. Closing mid-workout and reopening shows the same workout.

### M7: Result screen

- **Goal:** A short, motivating summary.
- **Files:** `app/result.tsx`, `src/progress/summarizeWorkout.ts`.
- **Approach:** "2 / 3 correct", streak, strongest area, keep practicing, one "Done" button. One subtle animation, no confetti storm.
- **Tests:** Summary for 3/3, 0/3 and ties. Screen renders.
- **Done when:** After the last challenge, the result shows the right score and areas.

### M8: Streak + local persistence

- **Goal:** Streak and history survive restarts. Storage problems never crash the app.
- **Files:** `src/progress/{streak,store}.ts`, `src/storage/{storage,schema,migrate}.ts`.
- **Approach:** Rules from section 5. Zustand `persist` → AsyncStorage. Schema version + migrate. Corruption fallback.
- **Tests:** Streak: first completion, consecutive days, missed day, two completions the same day, month and year boundaries, daylight saving, clock moved back. Storage: save/load round-trip, missing data, corrupted JSON, old-schema migration, reload from storage (simulated restart).
- **Done when:** Finish today → 🔥 1. Change the phone date to tomorrow and finish → 🔥 2. Skip a day → "Start a new streak" with best streak kept. Force-close and reopen keeps everything.

### M9: Basic progress

- **Goal:** A Progress screen plus a small summary on Home.
- **Files:** `src/progress/stats.ts`, `app/progress.tsx`, Home card.
- **Approach:** Workouts completed, challenges solved, accuracy, current and best streak, Tactics / Blunders / Decisions %. Show "—" until a category has 3+ answers.
- **Tests:** Empty, partial and full histories. Rounding.
- **Done when:** Numbers match a hand-checked example. The empty state reads well.

### M10: Polish

- **Goal:** Feels fast and pleasant.
- **Approach:** Piece move animation. Right/wrong micro-animations + haptics. Copy pass in beginner language. "Done for today" Home state. Drag-to-move. Placeholder icon and splash. Check small screens and large fonts.
  **Decision for you at that point:** an optional local daily reminder (expo-notifications, no server), asked only after the first finished workout.
- **Tests:** Interaction tests for the Home states.
- **Done when:** Cold start to Home feels instant on a mid-range Android phone (target under 2 s). Moves animate without stutter. All copy reviewed.

### M11: Testing hardening

- **Goal:** Confidence before strangers use it.
- **Approach:** Maestro flow: fresh install → finish workout → see 🔥 1 → relaunch → "done for today". Manual checklist: TalkBack, 200% font size, 360dp-wide phone, tablet, dark mode, airplane mode, low-end device.
- **Done when:** The Maestro flow passes, the checklist is done, and there are no known crashes.

### M12: Android release prep

- **Goal:** A closed test live on Google Play.
- **Approach:**
  - Final name + package name (permanent once published).
  - EAS Build `.aab`, Play App Signing, version numbers.
  - Confirm target API 36 (required for new apps and updates since Aug 31, 2026).
  - Icon, feature graphic, screenshots, privacy policy page, Data safety form, content rating.
  - Decide on crash reporting (e.g. Sentry). Update Data safety if added.
  - Closed test with 12+ testers for 14 days in a row (required for personal developer accounts created after Nov 13, 2023). Then production.
- **Done when:** Testers install from Play, and the kill/continue checkpoint is measured.

---

## 7. Risks

| Risk | Plan |
|---|---|
| Explanations are wrong or confusing | Generated only from engine-verified facts, plus your review. CI checks move legality. Testers flag bad ones |
| Spot the Blunder quality | Strict engine thresholds. Start with the clearest cases (hanging queen or rook, mate in 1) |
| Content runs out | 300 challenges = 100 days. The pipeline can make thousands more |
| Duolingo-sized competition | Narrow angle + kill/continue checkpoint |
| Play's 12-tester rule | Line up testers early: friends, local chess clubs, r/chessbeginners |
| Licensing mistakes | Only CC0, MIT, Apache or CC-BY assets. Stockfish never shipped |

---

## 8. Sources

Market:

- [Duolingo Q4 2025 earnings call (chess DAUs)](https://www.fool.com/earnings/call-transcripts/2026/05/04/duolingo-duol-q4-2025-earnings-transcript/)
- [Duolingo Chess PvP on Android (Marketech APAC)](https://marketech-apac.com/duolingo-launches-chess-pvp-mode-on-android-letting-learners-play-and-practise-languages/)
- [Duolingo Chess reviews: Chess.com blog](https://www.chess.com/blog/ArthurBuinovskiy/chess-in-duolingo), [David Rosales](https://davidwilliamrosales.com/2025/08/18/duolingo-chess-review/), [Fast Company](https://www.fastcompany.com/91317214/duolingo-will-start-teaching-chess-soon)
- [Chess.com membership plans](https://support.chess.com/en/articles/8562418-what-does-each-level-of-membership-get-me)
- [Chess.com passes 200M members](https://nerdschalk.com/chess-com-surpasses-200-million-members-as-platform-nears-20th-anniversary/)
- [Vidit Gujrathi launches chess with Physics Wallah (ChessBase India)](https://chessbase.in/news-bites/vidit-gujrathi-launches-chess-with-physics-wallah)
- [Chessmate by PW](https://www.pw.live/chess)
- [ChessMate on Google Play](https://play.google.com/store/apps/details?id=com.chessmate&hl=en_US)
- [Chess Training: Proven Drills (AppBrain)](https://www.appbrain.com/app/chess-training-proven-drills/com.shubi.chessTrainer)
- [blunder.clinic announcement](https://lichess.org/@/fruitdealer2002/blog/blunderclinic-dont-blunder/oNSyIUBb)
- [Daily Chess Puzzle Challenge](https://play.google.com/store/apps/details?id=com.netadapt.dailychesspuzzle&hl=en_US), [Chessle](https://play.google.com/store/apps/details?id=com.lupusapps.chessle&hl=en_US), [ChessLab Puzzle](https://apps.apple.com/us/app/-/id6757890503)
- [Noctie overview](https://dataconomy.com/tools/noctie/)
- [App retention benchmarks (Braze)](https://www.braze.com/resources/articles/mobile-app-retention), [AppsFlyer 2025 retention report](https://appsflyer.com/?p=453529)

Names:

- [BlunderProof (Chessmood)](https://chessmood.com/blog/stop-blunders-in-chess), [Blunder Proof Method](https://thechessworld.com/store/blunder-proof-method-with-fm-adrian-secheres/)
- [Lucky Chessmate (WIPO, via Trademark Elite)](https://www.trademarkelite.com/wipo/trademark/trademark-detail/1676284/Lucky-Chessmate)
- [Chessreps on Google Play](https://play.google.com/store/apps/details?id=com.chessreps.app&hl=en), [Chess Reps](https://play.google.com/store/apps/details?id=com.jonasmayer.openingmanager&hl=en_GB)
- [KnightCap engine](https://cgit.freebsd.org/ports/tree/games/KnightCap/pkg-descr), [Pawnder engine](https://chessprogramming.org/Pawnder)
- [PawnUp.com pawn shop](https://www.24-7pressrelease.com/press-release/252645/pawnupcom-online-pawn-shop-announces-holiday-hours-initiative)
- [QuietChess](https://julianperry.itch.io/quietchess)
- [SAVE A LIFE, LOOK TWICE](https://www.trademarkia.com/save-a-life-look-twice-77527593), [LOOK TWICE SAVE A LIFE](https://uspto.report/TM/86935004)
- [Play title limit: 30 characters](https://appdrift.co/blog/app-store-character-limits-complete-reference)
- [Can two apps have the same name?](https://appdrift.co/blog/check-if-app-name-is-taken), [Apple forums: name already used](https://developer.apple.com/forums/thread/691494)
- [IP India public search how-to](https://www.intepat.com/blog/trademark/conduct-trademark-public-search-india/)

Tech:

- [Expo SDK 57](https://expo.dev/changelog/sdk-57), [Expo SDK 58 beta](https://expo.dev/changelog/sdk-58-beta)
- [chess.js](https://cdn.jsdelivr.net/gh/jhlywa/chess.js@master/README.md)
- [react-native-chessboard](https://github.com/enzomanuelmangano/react-native-chessboard)
- [Lichess open database (CC0, puzzle format)](https://database.lichess.org/)
- [Lichess piece set licenses (COPYING.md)](https://github.com/lichess-org/lila/blob/master/COPYING.md)
- [Stockfish vs ChessBase (GPL)](https://lichess.org/blog/YtcjWhAAACcA48fo/stockfish-vs-chessbase-round-1)
- [stockfish npm package](https://npmjs.com/package/stockfish)
- [Google Play target API requirements](https://developer.android.com/google/play/requirements/target-sdk)
- [Google Play 12-tester rule (2026 guide)](https://www.testerscommunity.com/blog/google-play-closed-testing-requirements-2026)
- [AsyncStorage vs MMKV (2026)](https://reactnativerelay.com/article/react-native-mmkv-vs-asyncstorage-2026)
