# Install Skillman across AI coding agents

**Background Gremlin Group — Creating Unique Tools for Unique Individuals**

> Reviewed October 2026 against vendor documentation. Agent Skills is a portable format, not a guarantee that every model or product accepts the same installer, tools, or commands. This guide describes supported *agent hosts*, not model capabilities or endorsements.

## Choose a package

| Goal | Package |
|---|---|
| One skill with all 40 Codeman specialty guides | [Codemaster ZIP](../upload-zips/codemaster.zip) or [Codemaster directory](../skills/codemaster/) |
| One focused coding skill | [Individual skill ZIPs](../upload-zips/) or [skill directories](../skills/) |
| Offline collection for maintainers | [Full collection bundle](../bundles/skillman-all-public-skills.zip) |

**Web skill managers** typically accept a **standalone skill ZIP**. **Local coding agents** typically discover an **extracted skill directory** containing `SKILL.md` and its `references/`. The full-collection bundle is **not** a single installable skill. Codemaster is one skill entry point with 40 bundled specialist reference guides; it does not run 40 agents in parallel.

**Do not use `@Template Creator` to install Codemaster in ChatGPT.** Template Creator creates reusable artifact templates (such as documents or presentations). Codemaster is an existing *coding agent skill* and belongs in the Skills interface. Attaching a ZIP to an ordinary chat may let an agent inspect it, but is not the same as installing it persistently.

## ChatGPT

1. Download [codemaster.zip](../upload-zips/codemaster.zip) or a specific standalone ZIP.
2. On an eligible ChatGPT account, open **Plugins → Skills** in the sidebar.
3. Choose **Create → Upload from your computer** and select that one ZIP.
4. Review the upload scan, finish the installation, and start a new conversation.
5. Select the skill if offered or ask: **Use Codemaster to manage this programming project and verify all existing features remain intact.**

The official Skills guide lists eligible Business, Enterprise, Healthcare, and Edu accounts, subject to workspace policies and rollout. If you cannot see Skills or upload controls, check your account and administrator settings; uploading a ZIP as a normal chat attachment does not install it.

Source: [Skills in ChatGPT — OpenAI](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

## Claude.ai web

1. Download one standalone skill ZIP, such as [codemaster.zip](../upload-zips/codemaster.zip).
2. Open **Customize → Skills**.
3. Choose **+ → Create skill → Upload a skill**.
4. Select the ZIP containing the skill folder, enable it, and ask Claude to use **Codemaster**.

Custom-skill access depends on the plan and code-execution settings. A Claude web skill upload is distinct from manually installing a folder for Claude Code.

Sources: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) and [Create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

## Claude Code

Claude Code discovers a whole skill folder at `~/.claude/skills/<skill-name>/` for user scope or `.claude/skills/<skill-name>/` for a project.

From the extracted Skillman repository, on macOS/Linux:

```bash
mkdir -p "$HOME/.claude/skills"
cp -R skills/codemaster "$HOME/.claude/skills/"
```

For a target project, copy the complete `skillman/skills/codemaster` directory into that project's `.claude/skills/`. Launch Claude Code in the project; type `/codemaster` or request a matching task. Do not copy just `SKILL.md` without its references.

Source: [Claude Code skills — Anthropic](https://code.claude.com/docs/en/skills).

## OpenAI Codex CLI and IDE

Codex discovers user skills under `~/.agents/skills/` and repository skills under `.agents/skills/`.

```bash
mkdir -p "$HOME/.agents/skills"
cp -R skills/codemaster "$HOME/.agents/skills/"
```

Start Codex in the target project and type `/skills` or mention `$codemaster` in your prompt. Codex also supports asking its skill installer to fetch a skill from a GitHub repository. If a new skill is not visible, restart the session.

Source: [Build skills — OpenAI](https://learn.chatgpt.com/docs/build-skills).

## Google Gemini CLI

Gemini CLI discovers skills in `~/.gemini/skills/` (personal) and `.gemini/skills/` (project), plus compatible `.agents/skills/` locations.

```bash
mkdir -p "$HOME/.gemini/skills"
cp -R skills/codemaster "$HOME/.gemini/skills/"
gemini skills list
```

Run `/skills reload` in an active Gemini CLI session after adding a folder. Gemini also offers `gemini skills install` for repositories or local sources; use `gemini skills install --help` for the flags in your installed version. Skill activation may require consent.

Source: [Agent Skills — Gemini CLI](https://geminicli.com/docs/cli/skills/).

## Cursor

Cursor discovers `.cursor/skills/` and `.agents/skills/` project directories, and `~/.cursor/skills/` or `~/.agents/skills/` for local user scope.

```bash
mkdir -p .cursor/skills
cp -R /absolute/path/to/skillman/skills/codemaster .cursor/skills/
```

Open the target project in Cursor Agent, use `/codemaster` or select the skill through `@` when available, and check **Customize → Skills**. Global local skills are not automatically available in Cursor Cloud Agents without the host's synchronization settings.

Source: [Agent Skills — Cursor](https://cursor.com/docs/skills).

## GitHub Copilot

Supported Copilot agent surfaces discover project skills in `.github/skills/`, `.claude/skills/`, or `.agents/skills/`; personal paths include `~/.copilot/skills/` and `~/.agents/skills/`.

```bash
mkdir -p .github/skills
cp -R /absolute/path/to/skillman/skills/codemaster .github/skills/
```

Use a compatible Copilot Agent mode or CLI and request Codemaster by name. In Copilot CLI, check `/skills list` and reload when your installed version supports it. This skill does not grant GitHub permissions, enable paid Copilot features, or authorize hosted workflows.

Source: [Add agent skills — GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

## OpenCode

OpenCode discovers `.opencode/skills/` or `.agents/skills/` project directories, and `~/.config/opencode/skills/` or `~/.agents/skills/` user directories.

```bash
mkdir -p "$HOME/.config/opencode/skills"
cp -R skills/codemaster "$HOME/.config/opencode/skills/"
```

Start OpenCode and ask the agent to use **codemaster**. Its skill tool loads relevant instructions when needed.

Source: [Agent Skills — OpenCode](https://docs.opencode.ai/docs/skills/).

## Windows PowerShell for local agents

From the extracted Skillman checkout, install Codemaster into the shared user skills directory supported by Codex, Gemini CLI, Cursor, Copilot, and OpenCode:

```powershell
$destination = Join-Path $HOME '.agents\skills'
New-Item -Path $destination -ItemType Directory -Force | Out-Null
Copy-Item -Path '.\skills\codemaster' -Destination $destination -Recurse -Force
Test-Path (Join-Path $destination 'codemaster\SKILL.md')
```

The final command should return `True`. For **Claude Code**, replace `.agents\skills` with `.claude\skills`. To install an individual specialty, replace `codemaster` with its exact folder name.

## Share one local skill across multiple agents

Codex, Gemini CLI, Cursor, GitHub Copilot, and OpenCode all document support for the project-level `.agents/skills/<skill-name>/SKILL.md` layout. You can use that common location to avoid duplicate copies:

```bash
git clone https://github.com/bggg-gizmo/skillman.git
mkdir -p TARGET_PROJECT/.agents/skills
cp -R skillman/skills/codemaster TARGET_PROJECT/.agents/skills/
```

`TARGET_PROJECT` here is a directory name you choose; replace it with your actual project root. Claude Code uses `.claude/skills/` instead. File-system conventions and startup behavior vary by host and version.

## Verify installation and troubleshoot

1. Confirm a complete `codemaster/SKILL.md` is directly inside the selected skills directory, **with its references**; preserve the folder's relative paths.
2. Restart or reload the agent when its skills listing does not refresh.
3. Confirm the provider allows custom skills for your account and that your project is trusted.
4. Review instructions and bundled scripts before granting permissions; skills are not equivalent to tools, credentials, or unrestricted shell access.
5. Supply your own authorized projects and configuration; Skillman deliberately omits the creator's personal repositories and machine paths.
6. Ask for real build/test evidence and identify what could not run. Packaging validation alone does not prove a skill improves an agent's performance or prevents regressions.

## Upstream documentation

[OpenAI ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) · [OpenAI Codex](https://learn.chatgpt.com/docs/build-skills) · [Claude web](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Claude Code](https://code.claude.com/docs/en/skills) · [Gemini CLI](https://geminicli.com/docs/cli/skills/) · [Cursor](https://cursor.com/docs/skills) · [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) · [OpenCode](https://docs.opencode.ai/docs/skills/) · [Agent Skills standard](https://agentskills.io/specification).

These vendor names identify supported installation approaches; they do **not** imply endorsement, certification, identical tool availability, or measured performance on each platform.
