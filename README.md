### Latest news

🔊 2021/09/11: The IEEE SERVICES 2021 Hackathon is over. Thank you everybody for your submissions and contributions. The Hackathon committee awarded Anh Pham and Daniel Beaulieu for [QAOA Hierarchical Clustering](https://github.com/IEEEServices/hackathon-2021/issues/15) in the General category, and Abiskar Thapa, Freya Shah, Jaimil Dalwadi and Yoyo Liu for [The Traveling Salesman Problem](https://github.com/IEEEServices/hackathon-2021/issues/19) in the Student category. 🎉👏👏👏🎉

🔊 2021/09/03: The IEEE SERVICES 2021 Hackathon is now closed! Congratulations to all the teams that submitted and project 👏👏👏. Early next week we'll announce the preselected project to present at IEEE SERVICES 2021.

🔊 2021/08/09: All registered developers can now start experimenting with [Qiskit Runtime built-in programs](https://quantum-computing.ibm.com/services). They are public for using with simulators! 🎉🎉

🔊 2021/07/29: Now you can simulate launching Qiskit Runtime programs from a Web service with the [Qiskit Runtime test server](https://github.com/delapuente/qiskit-runtime/#test-server)! This is a special fork of the original Qiskit Runtime repository created for this hackathon.

## What is this about?
<!-- About IEEE Services Hackathon -->

<img src="/images/logo-icws-new.png" width="100">

IEEE Services Hackathon is an event collocated with the [2021 IEEE World Congress on Services](https://conferences.computer.org/services/2021/) (SERVICES 2021), and is sponsored by the IEEE Computer Society. The IEEE Computer Society established the services computing initiative two decades ago in response to the fast-growing service industry as well as the exponential rise in computing professionals.

# The cloud as a quantum-computing accelerator

>These machines, now called mainframes, were locked away in specially air conditioned computer rooms, with staffs of professional operators to run them. Only big corporations or major government agencies or universities could afford the multimillion dollar price tag. To run a job (i.e., a program or set of programs), a programmer would first write the program on paper (in FORTRAN or assembler), then punch it on cards. He would then bring the card deck down to the input room and hand it to one of the operators and go drink coffee until the output was ready.

–[A History of Operating Systems](http://www.cosy.sbg.ac.at/~clausen/PVSE2006/printerfriendly.asp.htm), Andrew S. Tanenbaum

Quantum Computing promises to be a revolutionary milestone in the history of cloud services. There will be a day that quantum processors become a commodity and they will speed up complex calculus in a similar way that GPUs are doing nowadays. Developers, all around the world, will benefit from the ultimate computational power. 

Until that date, quantum processors are a scarce resource, only available through the cloud, and working in a sort of a "batch mode", executing short, static, and noisy programs called [circuits](https://qiskit.org/textbook/ch-algorithms/defining-quantum-circuits.html#2.-What-is-a-Quantum-Circuit?-).

Despite the limited execution time, and the relatively high level of noise, the success of near-time quantum computing seems to be at the reach of our fingertips thanks to the intimate collaboration between classical and quantum computing. Cloud architectures leveraging colocation of classical and quantum resources, and reducing waiting times between the interacting parts, enable applicable fast, iterative dynamic workflows, where new circuits are created on the fly, according to the results of classical computations.

## Proposed task

We challenge the participants to create innovative cloud services on top of custom quantum programs or to find novel applications for the Qiskit Runtime's built-in library.

Introduced by IBM Quantum, [Qiskit Runtime](https://quantum-computing.ibm.com/lab/docs/iql/runtime/) is a new model of execution aiming at fulfilling the promises of near-time quantum computing by executing hybrid classical and quantum Python programs.

We envision a future of quantum services and invite all the community of professional developers, students and quantum enthusiasts to make the most of quantum cloud services using Qiskit Runtime. Even in beta, [developers can download and start experimenting locally](https://github.com/delapuente/qiskit-runtime/#test-server), leveraging built-in programs or uploading their own, and exposing them as cloud services for others to use.

## How to participate

Here you have a summary about how to participate. Along this README, you will find more details about the conference. We encourage reading it from begenning to end.

1. If you did not read the [code of conduct](https://github.com/Qiskit/qiskit/blob/master/CODE_OF_CONDUCT.md), start by reading it.
2. Choose a [category](#categories--prizes) to participate.
3. Find your [team members](#team-formation) and [register the project](https://github.com/IEEEServices/hackathon-2021/issues/new?assignees=&labels=&template=project-registration.md&title=Project+name). Do this as soon as possible, you can modify the project details later.
4. Participate:
    1. Download the beta version of [Qiskit Runtime + Test Server](https://github.com/delapuente/qiskit-runtime/)
    2. Learn how to [locally run a test server](https://github.com/delapuente/qiskit-runtime/blob/main/qiskit_runtime/test_server/README.md).
    3. Read about [accessing the REST API directly](https://github.com/delapuente/qiskit-runtime/blob/main/tutorials/API_direct.ipynb) and [writing your own programs](https://github.com/delapuente/qiskit-runtime/blob/main/qiskit_runtime/test_server/README.md#new-programs).
    4. Start hacking your idea!
6. Upon submission deadline on **August, 30th**, ensure that you...
    - License your project under the [Apache license 2.0](https://www.apache.org/licenses/LICENSE-2.0).
    - Write a [report](#project-report) explaning your project and upload it to https://arxiv.org
    - [Tag the final version](https://git-scm.com/book/en/v2/Git-Basics-Tagging) of your project with the tag `submission`.
7. Wait for [preselection](#evaluation-criteria).
8. Present at SERVICES 2021!
9. Wait for [winners announcement](#categories--prizes).

##  Motivating scenarios (use cases)

Many near-term quantum algorithms are variational, i.e., they involve an optimization loop between classical and quantum computers. For such algorithms the Qiskit Runtime is crucial to improve performance and to scale to larger systems. In the following we'll introduce the currently available Qiskit Runtimes and discuss possible applications:

**Variational Quantum Eigensolver (VQE) Runtime**: VQE is an algorithm to approximate the ground state of a given Hamiltonian by replacing the full exponential Hilbert space by a sub-space determined via a parametrized quantum circuit. A classical optimizer is then used to find the optimal parameters that minimize the expected value defined by the circuit and Hamiltonian. VQE can be applied in many domains, e.g. to find groundstates in quantum chemistry or to find good solutions to combinatorial optimization problems. Finding ground states is a fundamental task in chemistry and eventually will enable designing new materials, catalysts, etc. Combinatorial optimization is very difficult classically, since the number of possibilities scales exponentially with the number of variables. Possible applications range from portfolio optimization, to optimal routing, to protein folding.

**Quantum Approximate Optimization Algorithm (QAOA)**: One key question for VQE is how to chose the parametrized quantum circuit for a given problem. QAOA is a variant of VQE particularly suited for combinatorial optimization where the circuits are constructed based on the given problem and with some convergence guarantees if the circuits could be made long enough. Thus, QAOA has the same applications as VQE but is particularly suited for combinatorial optimization.

**Quantum Kernel Alignment (QKA)**: Quantum computers allow to evaluate kernels to be used e.g. in Support Vector Machines (SVM) on exponentially large feature spaces. This may help to improve the performance of machine learning models and lead to higher accuracies. QKA extends this idea to parametrized kernels that are trained to best match the data. The QKA Runtime allows to align to and evaluate the kernel for given data in the cloud and uses is it for classification tasks such as fraud detection.

**Your Awesome Program**: Collaboration has always been an important concept in the scientific community. 
In addition to using the build-in programs, you can come up with your own Qiskit Runtime programs that
can help you and others accelerate their research. Much like the existing built-in programs, your
new program will benefit the most from the Qiskit Runtime architecture if it requires iterative 
quantum/classical processing. Ideally, the program would be flexible enough to suite a wide range of 
applications but also easy to use.

## Code of Conduct

By participating in the IEEE Services 2021 hackathon, we all abide by the [Qiskit Code of Conduct](https://github.com/Qiskit/qiskit/blob/master/CODE_OF_CONDUCT.md), [IEEE Code of Conduct](https://www.ieee.org/content/dam/ieee-org/ieee/web/org/about/ieee_code_of_conduct.pdf) and [IEEE Code of Ethics](https://www.ieee.org/about/corporate/governance/p7-8.html)

If you are an observer or a victim of harassment, or any other behaviour against our codes of conduct, **direct your inquiry to one of the following contacts**:

Salvador de la Puente González - [salva@ibm.com](mailto:salva@ibm.com)

## Meeting point

Either if you are a participant looking for expert help, or a team in the search of coachers, or a coacher willing to help, we meet in Slack.

Access the [Qiskit Slack workspace](https://ibm.co/joinqiskitslack), and join the channel `#ieeeservices-hackathon-21`.

## Categories & prizes

There are two categories a team can participate in: student and general.

Best teams will receive a certificate, a prize in cash and the opportunity of presenting its proposal in a session at SERVICES 2021 conference.

## Projects & deliverables

To register a new project, fill the [Project Registration template](https://github.com/IEEEServices/hackathon-2021/issues/new?assignees=&labels=&template=project-registration.md&title=Project+name).

A team can only participate with one project. The deliverable is a GitHub repository including, at least:

- The source code of the project.
- A README file with instructions to test it<sup>*</sup>.
- A LICENSE file with the [Apache license 2.0](https://www.apache.org/licenses/LICENSE-2.0).
- A report with an [specific format](#project-report), detailed later.

<sup>*</sup>An easy way of testing the project is throught the use of [Docker containers](https://www.docker.com/resources/what-container) (i.e., local host service + local application emulation). The GitHub repository should detail the steps for repeatability using docker containers. 

## Submitting & submission deadline

All submissions need to be finalized by **Monday August 30, midnight Eastern Standard Time, Time zone in New York, NY (GMT-5)**.

Upon submission, [tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging) the version of the project you want to be evaluated with the tag `submission`.

Remember the repository should include all the files detailed in [Projects & deliverables](#project--deliverables).

##  Team formation

For team registration, add the names and institutions of the participants to your [project registration issue](https://github.com/IEEEServices/hackathon-2021/issues).

Teams participating in the student category will be composed only of students, not counting coachers.

Teams participating in the general category do not have any restriction but cannot have any coacher.

In any case, **a team cannot be more than 6 participants**, excluding coacher, and **a participant can join only one team**.

## Coachers

Teams of students can team up with one coacher from the industry and one coacher coming from the academia.

**Want to be a coacher?** Look at the [projects registered](https://github.com/IEEEServices/hackathon-2021/issues/) or [meet us on Slack](#meeting-point).

##  Project report

The report contextualizes the project and summarizes the software design process. It should contain **no more than eight pages** describing:

1. Motivation. _Why building the project?_
2. Innovation. _How original is the idea?_
3. Applicability. _What is the estimated time horizon, and the required conditions for practical applicability?_
4. Role of Qiskit Runtime. _Why the runtime plays a key role in the design?_
5. Future applications. _What is the potential future use once the technology has matured enough?_
6. Technology stack, design decisions, and architecture.

## Evaluation criteria

Once passed the [deadline](#submitting--submission-deadline), the hackathon committee will evaluate the projects according to the following criteria:

<!--
The evaluation will be conducted in Gavel platform based on pairwise comparison, based on Gavel's algorithm (https://www.anishathalye.com/2015/03/07/designing-a-better-judging-system). We will recommend our judges to consider following criteria when conducting pairwise comparisons.
-->

1.	Novelty of the idea (1 – 5 scale); 
2.	[Applicability](#project-report) (1 - 5 scale);
3.	Role of Qiskit Runtime (1 - 5 scale);
4.	Clarity of the report (1 – 5 scale);
5.	Easiness for setting up and using the system (1 – 5 scale);
6.	Performance, usability, and reliability of the system (1 - 5 scale)
7.	Code-base quality: learning curve to start contributing, code reliability, maintainability and documentation. (1 - 5 scale)

The hackathon committee will then preselect the best ones for presenting during IEEE SERVICES and, after evaluating the presentations, the hackathon committee will determine the winners of the hackathon.

## Learning materials

"Qiskit Runtime," IBM Quantum Lab documentation, 2021. [Online]. Available: https://quantum-computing.ibm.com/lab/docs/iql/runtime/. 

"Simulating Molecules using VQE," Qiskit Textbook, 2021. [Online]. Available: https://qiskit.org/textbook/ch-applications/vqe-molecules.html.

"Solving combinatorial optimization problems using QAOA," Qiskit Textbook, 2021. [Online]. Available: https://qiskit.org/textbook/ch-applications/qaoa.html. 

"Variational Quantum Linear Solver," Qiskit Textbook, 2021. [Online]. Available: https://qiskit.org/textbook/ch-paper-implementations/vqls.html.

"Quantum Kernel Alignment with Qiskit Runtime," Qiskit Runtime documentation, 2021. [Online]. Available: https://qiskit.org/documentation/partners/qiskit_runtime/tutorials/qka.html. 

##  References

B. Johnson and I. Faro, "IBM Quantum delivers 120x speedup of quantum workloads with Qiskit Runtime," IBM Research, 11-May-2021. [Online]. Available: https://research.ibm.com/blog/120x-quantum-speedup.
