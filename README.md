# Internet Computer Protocol (ICP)

> Smart contracts, canisters and dApps built on the **Internet Computer Protocol** using Rust and Kybra (Python on ICP).

[![ICP](https://img.shields.io/badge/Built%20on-Internet%20Computer-29ABE2?style=flat-square)](https://internetcomputer.org)
[![Rust](https://img.shields.io/badge/Rust-1.70+-orange?style=flat-square&logo=rust)](https://rust-lang.org)

## Overview

This repository contains smart contracts (canisters) and dApps deployed on the **DFINITY Internet Computer** — a decentralised cloud platform.

## Tech Stack

| Tool | Purpose |
|------|---------|
| Rust | Canister development |
| Kybra | Python-based canister SDK |
| DFX | DFINITY SDK / CLI |
| ICP | Deployment target |

## Project Structure

```
internet-computer-protocol/
├── src/           # Canister source code
├── portfolio/     # Portfolio canister
├── dfx.json       # DFX project config
└── canister_ids.json
```

## Getting Started

```bash
# Install DFX
sh -ci "$(curl -fsSL https://internetcomputer.org/install.sh)"

# Start local replica
dfx start --background

# Deploy canisters
dfx deploy
```

## License

MIT License — © 2025 Prasanga Pokharel
