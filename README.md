# Code4rena - Blockswap Formal Verification Contest with Certora
- Total Prize Pool: $30,000 USDC
  - HM awards: $16,500 USDC
  - Injected Bug awards: $10,500 USDC
  - Participation: $3,000 USDC
- Join [C4 Discord](https://discord.gg/code4rena) to register
- [Register](https://www.certora.com/workshops/code4rena-blockswap-1/) through Certora to gain access to the prover
  - Most information for installing and using the Certora Prover are available [here](doc.certora.com)
  - Additional resources to get familiar with the Certora Prover will be emailed to registrants along with their Certora key. 
- Starts January 19, 2023 20:00 UTC
- Ends February 2, 2023 20:00 UTC

---

# Notice

Please note that this is a formal verification contest and therefore many aspects of the contest are different from a traditional code4rena contest. Instead of just finding bugs, we are looking for implementations of properties in CVL (Certora Verification Language) which can either uncover bugs or prove properties of the contract always hold. Because of this key difference, the incentive model, participation, and submissions will be different. Please read this document in its entirety to ensure you fully understand the contest.

---

# Overview

Syndicate is a part of StakeHouse and facilitates distribution of EIP1559 rewards 50% to node runners and 50% to the Staking Funds Vault. For a more thorough overview of the StakeHouse protocol please check out the info in the [previous code4rena contest](https://github.com/code-423n4/2022-11-stakehouse) and documentation linked further down this file.

This challenge is about using the Certora prover to formally verify properties in the Solidity smart
contract `contracts/syndicate/Syndicate.sol`. There is a Certora specification file
`certora/specs/Syndicate.spec`, which can be used as a starting point. This specification
file can then be extended to add additional properties, which can then be verified by Certora. 

We will introduce several bugs in the syndicate smart contract, some of which are publicly available as .patch files in `certora/tests/certora/`. The rest of the bugs will be made public at the end of the contest and will be used to evaluate the properties proven. You can find more information on the incentive structure and participation instructions further down in this doc.

# Scope

| Contract | SLOC | Purpose | Libraries used |  
| ----------- | ----------- | ----------- | ----------- |
|[contracts/syndicate/Syndicate.sol](https://github.com/Certora/2023-01-blockswap-fv/blob/certora/contracts/syndicate/Syndicate.sol) [💰](#nowhere "Payable Functions") [📤](#nowhere "Initiates ETH Value Transfer")|[402](#nowhere "(nSLOC:374, SLOC:402, Lines:681)")|-|

# Additional Context

## Installation

This section explains 2 methods to install required dependencies to execute Certora on the
specification `certora/specs/Syndicate.spec`. The first method uses the docker file
located in the `docker` directory. The other method explains which tools need to be installed.

### Installing Manually

Installation instructions can be found [here](https://docs.certora.com/en/latest/docs/user-guide/getting-started/install.html?highlight=install). Briefly, you must install
* Node JS version >= 14.16.
* Yarn version >= 1.22.
* Java Development Kit version >= 11.
* Solidity version 0.8.13 (exactly this version).
* One can install Certora with the Python package manager Pip3,
  ```
  pip3 install certora-cli
  ```
* Assuming you are in the root of this reposotory, install the remaining dependencies with
  ```
  yarn install
  ```

### Installing With Docker

There is a docker file in the `docker` folder, with instructions to create an environment with
dependencies required for executing Certora. The container will be created with a user with
username 'docker' and password 'docker'. On a Unix system with an sh shell, the docker container
can be built with the `docker/build.sh` script. For example
```
docker/build.sh auto auto
```
builds the container with the docker user having the same user id and group id as the user executing
the `build.sh` script. The user id and group id are inferred using the `id` command. This is the
typical case.

If one wants to specify the user id and/or group id manually, then that is also possible. The first
argument to the `build.sh` script is the user id and the second argument is the group id,
```
docker/build.sh 1234 4321
```

When the container is built, then it can be started with the `docker/run.sh` script. For example
```
docker/run.sh "`realpath .`"
```
where the argument to `run.sh` is the absolute path to this repository (2023-01-blockswap-fv).
The repository will then be volume mapped for use inside the running docker container.

IMPORTANT: The docker container is automatically removed after exiting, so that all changes to the
container will be deleted. But since the repository 2023-01-blockswap-fv is volume mapped inside
the container, changes to the repository will be persistent, even after the docker container has
exited.

Inside the running docker container, go to the folder `~/2023-01-blockswap-fv` and run
```
yarn install
```
to install the last dependencies.

## Documentation on Certora

* The Certora documentation is located at https://docs.certora.com/en/latest/index.html
* There is a tutorial on Certora here https://github.com/Certora/Tutorials/blob/master/README.md

## Documentation on Blockswap LSD Networks (useful background knowledge).

To gain some background knowledge on the `Syndicate.sol` smart contract, it may be useful to take a
look at the following documentation:
* Blockswap LSD Networks https://docs.joinstakehouse.com/lsd/overview
* The StakeHouse protocol https://docs.joinstakehouse.com/protocol/learn/Stakehouse

---
# Formal Verification Contest Incentive Model
## Key Takeaways
* The objective is to prove strong properties and strength will be checked by testing the proven properties against 10 bugs, 3 of which are public from the start. Properties that catch real bugs are considered strong already.
* The total reward is split into three categories: participation, real bugs, and injected bugs
* Participation rewards are given to all security contributors that have a spec which catches publicly available injected bugs.
* Discrete injected bugs’ and real bugs’ awards are calculated similarly, using the [same equations as in normal Code4rena contests](https://docs.code4rena.com/awarding/incentive-model-and-awards). 
* Real bugs will require more details such as impact and an example exploit scenario.

## Incentives
A formal verification contest will still have a predefined total bounty which will be awarded in its entirety to security contributors. The specific distribution of rewards will be based on contributors’ performance. The rewards will be split into 3 categories and each category will have its own point system. The categories will be real bugs, injected bugs, and participation. 55% of the total bounty will be awarded to specifications catching real bugs, 35% to those catching the injected bugs and 10% for participation. In the case that no real bugs are found, participation pool will be increased to 22% and injected bugs pool will be increased to 78%.

The rewards for participating will be split equally among all eligible participants. To be eligible, participants must submit a specification which passes on the original code and fails on the publicly available injected bugs. The bugs will be provided by Certora and will be similar to the discrete injected bugs but will be part of the repo at the beginning of the contest.

The rewards for real bugs and injected bugs will be distributed very similarly, but since they are separate categories, the points for each category will be distinct. In both cases, contributors will receive points based on the bugs they discover. Each bug will start at a fixed total point value which will be split equally among all contributors if multiple contributors discover the same bug. The total points for a given bug will be reduced exponentially as the number of discoverers increases**. 

For real bugs, high and medium severity bugs will have a total value of 4 and 1 points respectively. Low severity bugs will not be accepted. Severity will be determined in the same way as [normal Code4rena contests](https://code4rena.com/judging-criteria/) with the contest being judged by Certora. To receive rewards for real bugs, submissions must describe the bug and include a rule that detects the bug. 

For discrete injected bugs and real bugs the  total number of points a bug is worth decreases as the number of discoverers increases. The value deteriorates based on the equation X * 0.9 ^ (n-1) where X is the initial value of the bug and n is the number of discoverers. This is put in place to prevent sybil attacks.

---
# Working Instructions for Formal Verification Contests
## Overview

* Create a private fork of the [public repository](https://github.com/Certora/2023-01-blockswap-fv) and give access to judges.
* Implement properties in the `certora-contest` branch.
* Set up all your scripts in the `certora/scripts` directory to check the specification against the code.
* Submit your work by creating a pull request from the `certora-contest` branch to the `certora` branch.

## Setup

To ensure other participants will not copy your properties, create a private fork of the [this repository](https://github.com/Certora/2023-01-blockswap-fv). Follow [this guide](https://medium.com/@bilalbayasut/github-how-to-make-a-fork-of-public-repository-private-6ee8cacaf9d3) to create a private mirror of the project (the final step in the guide is not necessary).

You’ll need to sync 2 branches on your fork:
* `certora-contest` - your working branch.
* `certora` - a reference branch that should not be touched unless instructed otherwise.

Make sure to grant read access to the judges `teryanarmen` and `vince0656` on GitHub.
Add a repository secret to your repo named `CERTORAKEY` with the key that will be emailed to you once you sign up through Certora (link is in the contest details above).

The forked repository will contain a `certora` directory that consists of 5 sub-directories - `harnesses`, `munged`, `scripts`, `tests` and `specs`. These should contain the entire preliminary setup to allow you to start writing rules. Each sub-directory contains a different component of the verification project and may contain additional sub-directories to maintain organization. Try to keep a similar structure when adding new files.

## Participation 

In the certora/spec directory, you will find a spec file named `Syndicate.spec`. In this spec, gather all the rules and invariants that you were able to verify. Some functions, definitions, and properties have been setup up for you to serve as an example. Before submitting this spec, make sure to check the following things:
* Add the `--rule_sanity` flag to your run script and check the entire spec to make sure that all rules are reachable at the time of submission. Rules that are not reachable will not be counted towards participation as they will not catch any bugs.
* Document each rule/invariant with a comment above that describes what the rule does in simple English. Any rule/invariant that isn’t documented will not be counted.
* It is recommended to inject a bug for each rule you write. This will ensure the rule is doing what you think it should be doing. To get more info on how to save injected bugs easily and undo changes, read the `README` in `certora/tests` and run `make help` from the certora directory.

**Do not leave failing rules or rules that are unreachable in Syndicate.spec.**

For rules that find issues, have a file named `SyndicateIssues.spec`, which contains only rules that fail and uncover issues in the code. For each rule that uncovers an issue/bug in the code, document each rule/invariant exactly as described for passing rules. In addition, above every rule, write the following extra information:
* A short and simple description of the attack vector described by the prover. Here you should elaborate on concrete values given by the prover if they exist, e.g., “ The withdraw function is prone to underflow - the balance before a withdrawal was 1, the amount to be withdrawn from the same address was 2, after the withdrawal, the balance is max_uint.”
* A short and simple description of the expected behaviour/values of the function, e.g., “in the case described above, the balance before is 1, and the amount to be withdrawn is greater than 1, we expect a revert to occur.”
* A reference to the line(s) of code that causes this issue.

**Do not leave unfinished rules/invariants in any of the spec files.**


## Testing

In the certora/scripts directory, you will find a run script(s) named `verifySyndicate.sh` that contains an example of a run script that can be used to run of your submitted spec files. You may need to configure these differently as you progress through the verification. Many of the options available are documented [here](https://docs.certora.com/en/latest/docs/prover/cli/options.html?highlight=script). It is recommended to test your spec against the publicly available injected bugs and bugs you injected to ensure your rules are working properly. You can do so by using the `verifyAllInjected.sh` script. This script will inject either the bugs injected by you or by certora one by one and run your spec against them.

## Submission

At the end of the formal verification contest, open a pull request within your repository from the `certora-contest` branch to the `certora` branch. Upon opening the PR, the CI will be triggered, running your spec against the publicly available injected bugs. **Make sure to add a `CERTORAKEY` as a repository action secret.** Also ensure that none of your run scripts have a `--send_only` flag.

A short time after the deadline, Certora will update the certora branch in the public repository with the additional non-released bugs. You will need to pull these changes to your repository’s `certora` branch. The CI will again be triggered and the result of the CI for these new jobs will be evaluated by the judges. If any additional changes need to be made once the discrete injected bugs are made public, please contact us first for permission. **Any changes made after the update without contacting Certora will result in disqualification.**

## Reporting Real Bugs
After finding a potential bug/unintended behaviour of the contract with the Certora Prover, write a short report according to the following template:
* Short description of the problem - 1-3 sentences.
* Elaborative explanation of the bug and an attack case example
  * Make sure to explain what’s the expected behaviour of the system.
  * What’s the actual behaviour of the system?
  * Try to plug in reasonable numbers to understand the damage that can be inflicted. Is the loss of funds bounded? 
* Property violated
  * Make sure to document the property that caught the issue according to the instructions specified in Participation

Open a git issue on your private repository with the information generated in the previous bullet.

For a period of time after the deadline, the judges will examine the bug and might contact you for clarifications. The goal of the meeting, in case it’s scheduled, is for the judges to get extra information and clarifications on the potential bug and the possible attack vector. To prepare for the meeting, please reread your report, refresh your memory on the issue, and consider planning a concrete example of an attack.
