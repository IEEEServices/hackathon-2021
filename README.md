## What is this about?
<!-- About IEEE Services Hackathon -->

<img src="/images/logo-icws-new.png" width="100">

IEEE Services Hackathon is an event collocated with the [2021 IEEE World Congress on Services](https://conferences.computer.org/services/2021/) (SERVICES 2021), and is sponsored by the IEEE Computer Society. The IEEE Computer Society established the services computing initiative two decades ago in response to the fast-growing service industry as well as the exponential rise in computing professionals.

<!--
For team and mentor registration, please go to the event website: https://ieeeservices.github.io/
-->



# The cloud as a quantum-computing accelerator

##  Introduction

>These machines, now called mainframes, were locked away in specially air conditioned computer rooms, with staffs of professional operators to run them. Only big corporations or major government agencies or universities could afford the multimillion dollar price tag. To run a job (i.e., a program or set of programs), a programmer would first write the program on paper (in FORTRAN or assembler), then punch it on cards. He would then bring the card deck down to the input room and hand it to one of the operators and go drink coffee until the output was ready.

–[A Hystory of Operating Systems](http://www.cosy.sbg.ac.at/~clausen/PVSE2006/printerfriendly.asp.htm), Andrew S. Tanenbaum

Quantum Computing promises to be a revolutionary milestone in the history of cloud services. There will be a day that quantum processors become a commodity and they will speed up complex calculus in a similar way that GPUs are doing nowadays. Developers, all around the world, will benefit from the ultimate computational power. 

Until that date, quantum processors are a scarce resource, only available through the cloud, and working in a sort of a "batch mode", executing short, static, and noisy programs called [circuits](https://qiskit.org/textbook/ch-algorithms/defining-quantum-circuits.html#2.-What-is-a-Quantum-Circuit?-).

Despite the limited execution time, and the relatively high level of noise, the success of near-time quantum computing seems to be at the reach of our fingertips thanks to the intimmate collaboration between classical and quantum computing. Cloud architectures leveraging colocation of classical and quantum resources, and reducing waiting times between the interacting parts, enable applicable fast, iterative dynamic workflows, where new circuits are created on the fly, according to the results of classical computations.

Proposed by IBM Quantum, [Qiskit Runtime](https://quantum-computing.ibm.com/lab/docs/iql/runtime/) is a new model of execution aiming at fulfilling the promises of near-time quantum computing by executing hybrid classical and quantum Python programs. Still in private beta, [developers can download and start experimenting locally](https://github.com/Qiskit-Partners/qiskit-runtime/), leveraging built-in programs or uploading their own and exposing them as cloud services for others to use.

<!--
### Scope of the challenge
-->


##  Motivating scenarios (use cases)

<!--

We give four use scenarios of the integrated mobility data to further analyze the requirements. Your solution should be focused on one scenario, which can be one of, but not limited to any of these scenarios.

•	Pandemic control and precaution. In this scenario, each individual voluntarily uploads their daily mobility histories, as well as health check information, e.g. whether they have coronavirus symptoms, whether they have contacted any coronavirus patients, and whether they have diagnosed with coronavirus. Then users who have been in the proximity of high-risk locations will be notified. 

•	Product recommendation. In this scenario, the service provider is able to collect the mobility history of each individual. These data will be used to analyze and infer the preference of each user and recommend restaurants, coffee shops, events, and so on.

•	User profile analysis. In this scenario, the service provider is able to collect mobility history of each individual and their preference information such as hobby, age, favourite books, educational level and so on. These data will be used to analyze and discover patterns of the group of users who frequently visit a certain location, which can be a restaurant, a coffee shop, an event and so on.

•	Map Service. In this scenario, each individual voluntarily uploads their daily mobility histories, and the data will be integrated with a map, so that it will visualize mobility at each location at different times. Users can also use this information to choose less popular places for shopping, travel and so on.

-->

##  Datasets and logistics

<!--
Each team should collect their own traces using Google Location Service from Google Takeout, and anonymize the data by themselves if needed.
-->

## Mentors

<!--
Reference technologies: 

differential privacy for deep learning, e.g., https://github.com/tensorflow/privacy

differential privacy for aggregation queries, e.g., https://github.com/google/differential-privacy

TEE and Intel-SGX, e.g., https://github.com/openenclave/openenclave

Python cryptograph libraries, e.g. https://github.com/pyca/cryptography
-->

## Learning materials

##  List of expected deliverables

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

# Evaluation criteria

<!--
The evaluation will be conducted in Gavel platform based on pairwise comparison, based on Gavel's algorithm (https://www.anishathalye.com/2015/03/07/designing-a-better-judging-system). We will recommend our judges to consider following criteria when conducting pairwise comparisons.


1.	Novelty of the idea (0 – 9 scale); 

2.	Privacy level and explanation (0 -9 scale)

3.	Clarity of the report (0 – 9 scale);

4.	Easiness for setting up and using the system (0 –9 scale);

5.	Performance, usability, and reliability of the system (0-9 scale)


#  Team Formation

A team should have no more than six persons;

#  Submission Deadline

All submissions need to be finalized by Monday Dec 21, noon Eastern Standard Time, Time zone in New York, NY (GMT-5). 
-->

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
