## What is this about?
<!-- About IEEE Services Hackathon -->

<img src="/images/logo-icws-new.png" width="100">

IEEE Services Hackathon is an event collocated with the [2021 IEEE World Congress on Services](https://conferences.computer.org/services/2021/) (SERVICES 2021), and is sponsored by the IEEE Computer Society. The IEEE Computer Society established the services computing initiative two decades ago in response to the fast-growing service industry as well as the exponential rise in computing professionals.

# The cloud as a quantum-computing accelerator

>These machines, now called mainframes, were locked away in specially air conditioned computer rooms, with staffs of professional operators to run them. Only big corporations or major government agencies or universities could afford the multimillion dollar price tag. To run a job (i.e., a program or set of programs), a programmer would first write the program on paper (in FORTRAN or assembler), then punch it on cards. He would then bring the card deck down to the input room and hand it to one of the operators and go drink coffee until the output was ready.

–[A Hystory of Operating Systems](http://www.cosy.sbg.ac.at/~clausen/PVSE2006/printerfriendly.asp.htm), Andrew S. Tanenbaum

Quantum Computing promises to be a revolutionary milestone in the history of cloud services. There will be a day that quantum processors become a commodity and they will speed up complex calculus in a similar way that GPUs are doing nowadays. Developers, all around the world, will benefit from the ultimate computational power. 

Until that date, quantum processors are a scarce resource, only available through the cloud, and working in a sort of a "batch mode", executing short, static, and noisy programs called [circuits](https://qiskit.org/textbook/ch-algorithms/defining-quantum-circuits.html#2.-What-is-a-Quantum-Circuit?-).

Despite the limited execution time, and the relatively high level of noise, the success of near-time quantum computing seems to be at the reach of our fingertips thanks to the intimmate collaboration between classical and quantum computing. Cloud architectures leveraging colocation of classical and quantum resources, and reducing waiting times between the interacting parts, enable applicable fast, iterative dynamic workflows, where new circuits are created on the fly, according to the results of classical computations.

## Proposed task

Introduced by IBM Quantum, [Qiskit Runtime](https://quantum-computing.ibm.com/lab/docs/iql/runtime/) is a new model of execution aiming at fulfilling the promises of near-time quantum computing by executing hybrid classical and quantum Python programs.

We envision a future of quantumn services and invite all the community of proffessional developers, students and quantum enthusiasts to make the most of quantum cloud services using Qiskit Runtime. Even in beta, [developers can download and start experimenting locally](https://github.com/Qiskit-Partners/qiskit-runtime/), leveraging built-in programs or uploading their own, and exposing them as cloud services for others to use.

We challenge the participants to create innovative cloud services on top of custom quantum programs or to find novel applications for the Qiskit Runtime's built-in library.

##  Motivating scenarios (use cases)

Many near-term quantum algorithms are variational, i.e., they involve an optimization loop between classical and quantum computers. For such algorithms the Qiskit Runtime is crucial to improve performance and to scale to larger systems. In the following we'll introduce the currently available Qiskit Runtimes and discuss possible applications:

**Variational Quantum Eigensolver (VQE) Runtime**: VQE is an algorithm to approximate the ground state of a given Hamiltonian by replacing the full exponential Hilbert space by a sub-space determined via a parametrized quantum circuit. A classical optimizer is then used to find the optimal parameters that minimize the expected value defined by the circuit and Hamiltonian. VQE can be applied in many domains, e.g. to find groundstates in quantum chemistry or to find good solutions to combinatorial optimization problems. Finding groundstates is a fundamental task in chemistry and eventually will enable designing new materials, catalysts, etc. Combinatorial optimization is very difficult classically, since the number of possibilities scales exponentially with the number of variables. Possible applications range from portfolio optimization, to optimal routing, to protein folding.

**Quantum Approximate Optimization Algorithm (QAOA)**: One key question for VQE is how to chose the parametrized quantum circuit for a given problem. QAOA is a variant of VQE particularly suited for combinatorial optimization where the circuits are constructed based on the given problem and with some convergence guarantees if the circuits could be made long enough. Thus, QAOA has the same applications as VQE but is particularly suited for combinatorial optimization.

**Quantum Kernel Alignment (QKA)**: Quantum computers allow to evaluate kernels to be used e.g. in Support Vector Machines (SVM) on exponentially large feature spaces. This may help to improve the performance of machine learning models and lead to higher accuracies. QKA extends this idea to parametrized kernels that are trained to best match the data. The QKA Runtime allows to align to and evaluate the kernel for given data in the cloud and uses is it for classification tasks such as fraud detection.

<!--
Add "upload your own program".
-->

## How to participate

Here you have a summary about how to participate. Along this README, you will find more details about the conference. We encourage reading it from begenning to end.

1. Choose a [category](#categories-prizes) to participate.
2. Find your [team members](#team-formation) and [register the project](https://github.com/IEEEServices/hackathon-2021/issues/new?assignees=&labels=&template=project-registration.md&title=Project+name). Do this as soon as possible, you can modify the project details later.
3. Start hacking!
4. Upon submission deadline on **September, 30th**, ensure that you...
  - License your project under the [Apache license 2.0](https://www.apache.org/licenses/LICENSE-2.0).
  - Write a [report](#project-report) explaning your project and upload it to https://arxiv.org
  - [Tag the final version](https://git-scm.com/book/en/v2/Git-Basics-Tagging) of your project with the tag `submission`.
5. Wait for [winners announcement](#categories-and-prizes).
6. Present at SERVICES 2021!

## Categories & prizes

There are two categories a team can participate in: student and general.

Best teams will receive a certificate, a prize in cash and the opportunity of presenting its proposal in a session at SERVICES 2021 conference.

##  Submissions & submission deadline

All submissions need to be finalized by Monday September 30, midnight Eastern Standard Time, Time zone in New York, NY (GMT-5).

A team can only participate with one submission. The submission is a GitHub repository with a piece of software, and a report detailed [later in this document](#project-report).

By the deadline, the repository must be licensed under the [Apache license 2.0](https://www.apache.org/licenses/LICENSE-2.0), include the [tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging) `submission`, marking the final version of the submission, and contain the report. The report must be upload to [arxiv.org](https://arxiv.org) too.

##  Team formation

For team registration, fill the [Team Registration template](https://github.com/IEEEServices/hackathon-2021/issues/new?assignees=&labels=&template=team-registration.md&title=Team+registration) and click on "Submit new issue".

Teams participating in the student category will be composed only of students, not counting mentors.

Teams participating in the general category do not have any restriction but cannot have any mentor.

In any case, **a team cannot be more than 6 participants**, excluding mentors, and **a participant can join only one team**.

## Mentors

Teams of students can team up with one mentor from the industry and one mentor coming from the academia. [Find your mentor](https://airtable.com/shrxy3zEj8wM5ipLR)!

**Want to be a mentor?** [Register](https://airtable.com/shr1CbDksw2htnG48), access the [Qiskit Slack workspace](https://ibm.co/joinqiskitslack), and join the channel `#ieeeservices-hackathon-21`.

##  Project report

<!--
#### Source code that must be uploaded to an open GitHub repository and must have a well-documented README file describing the steps of using the product;

#### Video recording of demonstration that must be uploaded to YouTube;

#### A report no more than 6 pages that describes:

1. The motivation,

2. Use scenario,

3. At which level privacy preserving is provided and explanation of how privacy preserving is provided,

4. Technologies used,

5. Novelty of the product; 

The report must either contain the url to the GitHub repository or the link to the YouTube video.

#### An emulation of the application should be easily setup in one desktop through docker containers (i.e., local host service + local application emulation). The GitHub repository should detail the steps for repeatability using docker containers. 
-->

## Evaluation criteria

<!--
The evaluation will be conducted in Gavel platform based on pairwise comparison, based on Gavel's algorithm (https://www.anishathalye.com/2015/03/07/designing-a-better-judging-system). We will recommend our judges to consider following criteria when conducting pairwise comparisons.


1.	Novelty of the idea (0 – 9 scale); 

2.	Privacy level and explanation (0 -9 scale)

3.	Clarity of the report (0 – 9 scale);

4.	Easiness for setting up and using the system (0 –9 scale);

5.	Performance, usability, and reliability of the system (0-9 scale)
-->


## Learning materials


##  References

<!--
[1] Dwork, C. (2008, April). Differential privacy: A survey of results. In International conference on theory and applications of models of computation (pp. 1-19). Springer, Berlin, Heidelberg.

[2] Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. Foundations and Trends in Theoretical Computer Science, 9(3-4), 211-407.

[3] Costan, Victor, and Srinivas Devadas. "Intel SGX Explained." IACR Cryptol. ePrint Arch. 2016, no. 86 (2016): 1-118.

[4] Gentry, Craig, Amit Sahai, and Brent Waters. "Homomorphic encryption from learning with errors: Conceptually-simpler, asymptotically-faster, attribute-based." Annual Cryptology Conference. Springer, Berlin, Heidelberg, 2013.

[5] Yang, Q., Liu, Y., Chen, T., & Tong, Y. (2019). Federated machine learning: Concept and applications. ACM Transactions on Intelligent Systems and Technology (TIST), 10(2), 1-19.

[6] Konečný, Jakub, et al. "Federated learning: Strategies for improving communication efficiency." arXiv preprint arXiv:1610.05492 (2016).

[7] Sheth, Amit P., and James A. Larson. "Federated database systems for managing distributed, heterogeneous, and autonomous databases." ACM Computing Surveys (CSUR) 22, no. 3 (1990): 183-236.

[8] McSherry, Frank, and Ilya Mironov. "Differentially private recommender systems: Building privacy into the netflix prize contenders." Proceedings of the 15th ACM SIGKDD international conference on Knowledge discovery and data mining. 2009.

-->
