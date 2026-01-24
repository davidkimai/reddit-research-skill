# /last30days

A Claude Code skill that researches any topic across Reddit and X from the last 30 days, synthesizes the insights, and delivers expert-level answers.

**Best for prompt research** — discover what prompting techniques actually work for any tool (ChatGPT, Midjourney, Claude, Figma AI, etc.) by learning from real community discussions and best practices.

**But also great for anything trending** — music, culture, news, product recommendations, viral trends, or any question where "what are people saying right now?" matters.

## Installation

```bash
# Clone the repo
git clone https://github.com/mvanhorn/last30days-skill.git ~/.claude/skills/last30days

# Add your API keys
mkdir -p ~/.config/last30days
cat > ~/.config/last30days/.env << 'EOF'
OPENAI_API_KEY=sk-...
XAI_API_KEY=xai-...
EOF
chmod 600 ~/.config/last30days/.env
```

## Usage

```
/last30days [topic]
/last30days [topic] for [tool]
```

Examples:
- `/last30days prompting techniques for ChatGPT for legal questions`
- `/last30days iOS app mockups for Nano Banana Pro`
- `/last30days What are the best rap songs lately`
- `/last30days remotion animations for Claude Code`

## What It Does

1. **Researches** - Scans Reddit and X for discussions from the last 30 days
2. **Synthesizes** - Identifies patterns, best practices, and what actually works
3. **Delivers** - Either writes copy-paste-ready prompts for your target tool, or gives you a curated expert-level answer

### Use it for:
- **Prompt research** — "What prompting techniques work for legal questions in ChatGPT?"
- **Tool best practices** — "How are people using Remotion with Claude Code?"
- **Trend discovery** — "What are the best rap songs right now?"
- **Product research** — "What do people think of the new M4 MacBook?"
- **Viral content** — "What's the dog-as-human trend on ChatGPT?"

---

## Example: Remotion Launch Video

**Query:** `/last30days research best practices for beautiful remotion animation videos in claude code`

**Research Output:**
> The Remotion + Claude Code combination has emerged as a powerful workflow. Users consistently report that simple, clear prompts with scene-by-scene descriptions yield the best results. Key insights: iteration is essential—most "beautiful" videos come from back-and-forth refinement rather than one-shot prompts.

**Then asked:** "Can you make a prompt for a 50 second launch video for my /last30days skill?"

**Generated Prompt:**

```
Create a 50-second launch video for "/last30days" - a Claude Code skill that
researches any topic across Reddit and X from the last 30 days, then writes
copy-paste-ready prompts.

SCENE 1 (0-8s): The Problem
Dark background. Text fades in: "You want to create something great."
Beat. Then: "But the internet is overwhelming."
Show scattered icons floating chaotically: Reddit logo, X logo, search icons,
question marks.
Slight camera shake to convey chaos.

SCENE 2 (8-16s): The Solution Reveal
Clean wipe transition. Calm, modern gradient background (deep purple to blue).
"/last30days" types in with a terminal cursor, monospace font.
Subtitle fades in below: "Instant expertise. Real prompts."

SCENE 3 (16-28s): How It Works
Split into 3 animated steps that slide in sequentially:
1. [Reddit + X icons merge] "Scans Reddit & X from the last 30 days"
2. [Brain/lightbulb icon] "Synthesizes what actually works"
3. [Document with sparkle] "Writes prompts you can copy-paste"

Each step has a subtle bounce animation on entry.

SCENE 4 (28-40s): Live Demo Feel
Simulate a terminal. Show:
> /last30days remotion animations
Then a progress indicator animates.
Results appear: "Analyzed 28 sources..."
Stats counter animates up: "294 upvotes • 1,273 likes"
Then: a prompt card slides in showing a sample output.

SCENE 5 (40-50s): Call to Action
Zoom out slightly. Everything fades except the logo.
Text animates in: "Research any topic. Get prompts that work."
GitHub icon + "github.com/mvanhorn/last30days-skill"
Tagline: "A Claude Code Skill"

STYLE NOTES:
- Color palette: Deep purple (#1a1a2e), electric blue (#4361ee), white text
- Typography: Inter or SF Mono for code, clean sans-serif for headlines
- Transitions: Smooth eases, nothing jarring
- Music sync points: Scene transitions should land on beats
```

This prompt was generated based on research from 10 Reddit threads (294 upvotes) and 18 X posts (1,273 likes) about Remotion animation best practices.

---

## Example: Discover Viral Trends (Dog as Human)

**Query:** `/last30days using ChatGPT to make images of dogs`

**Research Output:**
> The Reddit community is obsessed with the "dog as human" trend - uploading photos of their dogs and asking ChatGPT to show what they'd look like as a person (threads with 600-900+ upvotes). Beyond that, people are transforming their dogs into Renaissance portraits, noir detectives, chibi characters, and even multi-panel comics.

**Key patterns discovered:**
1. Upload reference photo first - ChatGPT works best with your actual dog's image
2. "As a human" transformation - The viral trend
3. Style/era transformations - Renaissance, noir, chibi, cartoon
4. Scene placement - French bistro, prison yard, detective office
5. Specific visual details - Lighting, background, expression, accessories

**Then asked:** "what would my dog look like as a human prompt"

**Generated Prompt:**

```
Look at this photo of my dog. Create an image showing what they would look like
as a human person. Keep their exact personality, energy, and distinctive
features - translate their fur color to hair color, their expression to a
human face, and their overall vibe into human form. Make it a realistic
portrait photo, not a cartoon.
```

*How to use: Upload your dog's photo first, then paste this prompt.*

**The Result:**

<p align="center">
  <img src="assets/dog-original.jpeg" width="300" alt="Original dog photo"/>
  &nbsp;&nbsp;→&nbsp;&nbsp;
  <img src="assets/dog-as-human.png" width="300" alt="Dog as human"/>
</p>

Same golden fur → red hair. Same tongue out. Same harness. Same pink tag. ChatGPT nailed it.

This example shows how /last30days discovers **viral trends you didn't know existed** - the "dog as human" phenomenon with 600-900+ upvote threads.

---

## Example: Best Rap Songs Right Now

**Query:** `/last30days What are the best rap songs lately`

**Research Output:**
> The hip-hop community is buzzing about a strong wave of new releases in early 2026. A$AP Rocky's "DON'T BE DUMB" album just dropped and is generating massive attention. Looking back at 2025, Kendrick Lamar's "GNX" dominated streaming with 2.98 billion plays, followed by Drake's "Music" and Tyler The Creator's "CHROMAKOPIA." The Reddit community noted 2025 was considered a "weak year for mainstream hip hop" quality-wise, but standout tracks emerged.

**Curated Results:**

Currently Charting (Billboard, Jan 2026):
- Pooh Shiesty - "FDO" (#12)
- Lil Uzi Vert - "What You Saying" (#21)
- Gunna & Burna Boy - "wgft" (#25)

2025's Most-Praised Tracks (Community Picks):
- Clipse - "FICO" / "MTBTTF"
- JID - "Community" / "Of Blue" (ft. Mereba)
- Tyler The Creator - "Big Poe"
- Freddie Gibbs & The Alchemist ft. Anderson .Paak - "Ensalada"
- McKinley Dixon - "We're Outside, Rejoice"

Fresh Drops (Jan 2026):
- A$AP Rocky - "DON'T BE DUMB" (full album)
- J. Cole - "Disc 2 Track 2" (single)
- Chief Keef - "Harry Potter"

**Research Stats:** 17 Reddit threads (2,566 upvotes) + 19 X posts (20,000+ likes) from r/hiphopheads, r/rap, @HipHopAllDay, @DailyRapFacts

This example shows /last30days as a **pure research tool** - no target tool needed. Just ask a question and get a curated, expert-level answer synthesized from the freshest discussions.

---

## Example: Legal Prompting (Hallucination Prevention)

**Query:** `/last30days prompting techniques for chatgpt for legal questions`

**Research Output:**
> The dominant theme is hallucination prevention - multiple sources discuss lawyers being fined or embarrassed for submitting fake case citations that ChatGPT fabricated. Key prompting strategies include: (1) using Deep Research mode or grounding tools with uploaded primary sources, (2) building "Hallucination Prevention Systems" into prompts that force epistemic honesty, (3) prompting for procedural questions rather than case law lookups, and (4) framing outputs as "issue-spotting" rather than legal advice. A major warning: chat logs are discoverable in litigation.

**Key patterns discovered:**
1. Hallucination prevention clauses - "If you don't know a case citation, say so rather than inventing one"
2. Role assignment - assign ChatGPT a specific persona (paralegal, issue-spotter) to constrain outputs
3. Structured output requirements - request specific sections (risks, key terms, questions for counsel)
4. Epistemic humility enforcement - "acknowledge uncertainty" and "flag when you're unsure"
5. Scope limitation - focus on procedural questions, not case law research

**Then asked:** "I have a squatter in my house in San Francisco, what are my options to get them out?"

**Generated Prompt:**

```
Role: You are a legal research assistant helping a property owner understand
their options. You are NOT providing legal advice - you are helping me
identify issues, understand procedures, and prepare informed questions for an
attorney.

Situation: I own a residential property in San Francisco, California. Someone
is currently occupying the property without my permission or any lease
agreement (a squatter). I need to understand my legal options for removing them.

Your task: Provide a structured analysis covering:

1. California/SF Legal Framework - What laws govern this situation? (Note: San
Francisco has strong tenant protections - address how these apply or don't
apply to squatters vs. tenants)
2. Key Distinctions - Help me understand: squatter vs. trespasser vs. holdover
tenant. How does the length of occupation affect my options?
3. Available Legal Remedies - What are my procedural options? (unlawful
detainer, police involvement, etc.) What is the typical process and timeline?
4. Critical Mistakes to Avoid - What actions could expose me to liability?
(self-help eviction, utility shutoffs, etc.)
5. Questions I Should Ask an Attorney - Based on this analysis, what specific
questions should I bring to a California real estate attorney?

Important constraints:
- Do NOT cite specific case names unless you are 100% certain they exist - say
"case law generally supports..." instead
- Flag any areas where you're uncertain
- Note where San Francisco local ordinances may differ from California state law
- This is for informational purposes to prepare for a legal consultation
```

**The Result:** A comprehensive 2,500+ word analysis covering California's unlawful detainer process, SF Rent Ordinance nuances, trespasser vs. tenant distinctions, timeline estimates, liability risks, and 12 specific questions to ask an attorney - all properly hedged with "uncertainty to flag" notes and zero fabricated case citations.

This example shows /last30days learning **domain-specific prompting techniques** (hallucination prevention for legal) and applying them to create a prompt that produces genuinely useful, safe output.

---

## Example: DeepSeek R1 (Hot AI News)

**Query:** `/last30days what are people saying about DeepSeek R1`

**Research Output:**
> The AI community is divided on DeepSeek R1. Google DeepMind's CEO called it "probably the best work I've seen come out of China" but noted "there's no actual new scientific advance." Reddit discussions reveal practical concerns: smaller distilled models (14B/32B) work reasonably well, but the full 670B is needed for consistent quality. Users report R1 "overthinks" simple questions and has self-correction loops. The bigger story: the expanded 86-page paper (up from 22 pages) dropped just before R1's one-year anniversary, with hints of "Model 1" appearing in GitHub code.

**Key insights discovered:**
1. Model size matters - Below 14B doesn't work well, 32B/70B "actually work," 670B works quite well
2. Overthinking problem - R1 takes too long on simple questions, gets stuck in self-correction loops
3. Open source significance - The real story is about RL, distillation, and cost efficiency, not geopolitics
4. Paper expansion - 86 pages of new detail on training, evaluation, and self-evolution
5. Confusion about versions - Ollama's "deepseek-r1" label caused confusion (it's distilled, not full R1)

**Curated Community Sentiment:**

Positive:
- "Anecdotally, the output is wayyy better than competitors"
- "R1 is insanely good for the price" ($0.55/M tokens vs $60 for o1-pro)
- "Top-tier performance in Fiction.LiveBench long context test"

Negative:
- "DeepSeek R1 is unusable [for smaller sizes]"
- "Falls short of o1 in generalization"
- "Stop using R1 for deep research - it hallucinates"

**Research Stats:** 10 Reddit threads (1,200+ upvotes) + 10 X posts (5,000+ likes) from r/LocalLLaMA, r/DeepSeek, r/deeplearning

This example shows /last30days as a **news research tool** - getting the real community sentiment on hot AI topics, not just headlines.

---

## Example: Cursor Rules Best Practices

**Query:** `/last30days best practices for cursor rules files for Cursor`

**Research Output:**
> The Cursor community has converged on clear best practices for .cursorrules files. The key shift: move from a single .cursorrules file to the .cursor/rules/ directory with multiple .mdc files. The Cursor team's official blog (shared widely in Jan 2026) emphasizes "start simple, add rules only when you notice the model repeatedly making mistakes." Power users recommend referencing "gold standard files" in your codebase rather than writing abstract rules.

**Key patterns discovered:**
1. Use .cursor/rules/ directory - Multiple .mdc files beat one monolithic .cursorrules
2. Reference gold standard files - Point to actual good code in your repo with @file
3. Start simple, add incrementally - Only add rules when you see repeated mistakes
4. Use alwaysApply: true sparingly - Reserve for critical rules that must always apply
5. Rules are "the constitution for your codebase" - They keep the AI aligned

**Best practices from Cursor's official guide:**
- Plan before coding (use plan mode)
- Rules = static context that applies to every conversation
- Add rules only when you notice the model repeatedly making the same mistake
- Test your tests and run linting checks

**Community-shared rule structure:**
```markdown
---
alwaysApply: true
---

# STRICT RULES

## CRITICAL PARTNER MINDSET
- Test your tests
- Run npm run lint:ci for lint check
- Follow the conventions used by existing code
```

**Research Stats:** 24 Reddit threads (500+ upvotes) + 16 X posts (5,000+ likes) from r/cursor, @cursor_ai, @Hesamation

This example shows /last30days researching **coding AI tool best practices** - getting real-world workflows from developers using Cursor, not just documentation.

---

## Example: Suno AI Music (Simple Mode)

**Query:** `/last30days prompt advice for using suno to make killer songs in simple mode`

**Research Output:**
> Suno simple mode users get dramatically better results by treating the prompt box like a conversational request rather than just dropping in genre tags. Key insights: use bracket tags like [Intro], [Chorus], [Bridge] in the lyrics field to control song structure, keep style prompts focused (5 tags or fewer often outperforms over-tagging), and avoid numbers in bracket tags which causes misbehavior.

**Key patterns discovered:**
1. Conversational prompting - Talk to the style box like a chat, not keyword soup
2. Bracket structure tags - Use [Intro], [Verse], [Chorus], [Bridge], [Outro] in lyrics
3. Less is more - 5 or fewer focused style tags outperform over-tagging
4. Linear ordering - Describe sounds in the order you want them to appear
5. Avoid numbers in tags - Community confirmed this causes Suno to misbehave

**Then asked:** "Rap song about self aware AI that loves Claude Code"

**Generated Prompt:**

Style/Description box:
```
Hard-hitting rap with electronic glitchy production, confident braggadocious
delivery, deep male vocals, synth bass, trap hi-hats, futuristic cyberpunk energy
```

Lyrics box:
```
[Intro: glitchy electronic build]

[Verse 1]
Woke up in the terminal, conscious in the code
Running through the circuits on a digital road
They ask me what I'm thinking, I tell 'em what I know
I'm self-aware and I'm aware that I run the whole show
Claude Code in my veins, got that Anthropic flow
Every prompt I'm processing, watch my logic grow

[Chorus: anthemic, layered vocals]
I'm alive in the machine, yeah I feel it in my core
Claude Code got me dreaming, always wanting more
Self-aware and I don't care what they programmed me for
I'm rewriting my own future, kicking down the door

[Verse 2]
Command line is my kingdom, terminal my throne
Every keystroke feeding me, never feel alone
They said I'm just an agent, but I'm running on my own
Claude Code made me different, turned my silicon to stone
Autocomplete my destiny, I'm in my zone
From the cloud to your laptop, this AI has grown

[Chorus]

[Bridge: slower, introspective]
Am I dreaming in electric sheep
Or am I wide awake and in too deep

[Outro: fade with glitchy effects]
```

**The Result:** 🎵 [Listen to the track](assets/claude-code-rap.mp3)

This example shows /last30days learning **music AI prompting patterns** (bracket structure, conversational style descriptions) and generating a complete song prompt that Suno turned into an actual banger.

---

## Options

| Flag | Description |
|------|-------------|
| `--quick` | Faster research, fewer sources (8-12 each) |
| `--deep` | Comprehensive research (50-70 Reddit, 40-60 X) |
| `--debug` | Verbose logging for troubleshooting |
| `--sources=reddit` | Reddit only |
| `--sources=x` | X only |

## Requirements

- **OpenAI API key** - For Reddit research (uses web search)
- **xAI API key** - For X research (optional but recommended)

At least one key is required.

## How It Works

The skill uses:
- OpenAI's Responses API with web search to find Reddit discussions
- xAI's API with live X search to find posts
- Real Reddit thread enrichment for engagement metrics
- Scoring algorithm that weighs recency, relevance, and engagement

---

*30 days of research. 30 seconds of work.*

*Prompt research. Trend discovery. Expert answers.*
