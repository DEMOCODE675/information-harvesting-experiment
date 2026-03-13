# information-harvesting-experiment

A GSOC 2026 experiment project from OWASP/OPENcre module A - Information Harvesting.

Module A – Information Harvesting (Pre-Code Experiment)

This repository contains the pre-code experiments for the OWASP OpenCRE Scraper & Indexer Module A.

Implemented experiments:

1. Junk file regex filter to remove non-relevant files.
2. Diff paragraph extractor using git diff.
3. YAML-based repository configuration parser.
4. GitHub API demo to fetch commits from OWASP repositories.

These experiments validate the core techniques required for the nightly information harvesting pipeline.

## Experiment Data Source

For testing the diff extraction and commit detection logic, I used several OWASP repositories as experiment sources.

Example repository used:

- OWASP CheatSheetSeries

These repositories were **not included in this project** and were only used to observe real-world Markdown changes and commit activity.

This repository contains only experimental code and does not redistribute any OWASP project source code.
