[Skip to content](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/#developer-experience-devex)

# Developer Experience (DevEx)

Developer experience refers to how easy or difficult it is for a developer to perform essential tasks needed to implement a change. A positive developer experience would mean these tasks are relatively easy for the team (see measures below).

The essential tasks are identified below.

- Build - Verify that changes are free of syntax error and compile.
- Test - Verify that all automated tests pass.
- Start - Launch end-to-end to simulate execution in a deployed environment.
- Debug - Attach debugger to started solution, set breakpoints, step through code, and inspect variables.

If effort is invested to make these activities as easy as possible, **the returns on that effort will increase the longer the project runs, and the larger the team is**.

## Defining End-to-End

This document makes several references to running a solution end-to-end (aka E2E). End-to-end for the purposes of this document is scoped to the software that is owned, built, and shipped by the team. Systems owned by other teams or third-party vendors is not within the E2E scope for the purposes of this document.

## Goals

- Maximize the amount of time engineers spend on writing code that fulfills story acceptance and done-done criteria.
- Minimize the amount of time spent manual setup and configuration of tooling
- Minimize regressions and new defects by making end-to-end testing easy

## Impact

Developer experience can have a significant impact on the efficiency of the day-to-day execution of the team. A positive experience can pay dividends throughout the lifetime of the project; especially as new developers join the team.

- Increased Velocity - Team spends less time on non-value-add activities such as dev/local environment setup, waiting on remote environments to test, and rework (fixing defects).
- Improved Quality - When it's easy to debug and test, developers will do more of it. This will translate to fewer defects being introduced.
- Easier Onboarding & Adoption - When dev essential tasks are automated, there is less documentation to write and, subsequently, less to read to get started!

**Most importantly, the customer will continue to accrue these benefits long after the code-with engagement.**

## Measures

### Time to First E2E Result (aka F5 Contract)

Assuming a laptop/pc that has never run the solution, how long does it take to set up and run the whole system end-to-end and see a result.

### Time To First Commit

How long does it take to make a change that can be verified/tested locally. A locally verified/tested change is one that passes test cases without introducing regression or breaking changes.

## Participation

Providing a positive developer experience is a team effort. However, certain members can take ownership of different areas to help hold the entire team accountable.

### Dev Lead - Set the Bar

The following are examples of how the Dev Lead might set the bar for dev experience

- Determines development environment (suggested IDE, hosting, etc)
- Determines source control environment and number of repos required
- Given development environment and repo structure, sets expectations for team to meet in terms of steps to perform the essential dev tasks
- Nominates the DevEx Champion

IDE choice is NOT intended to mandate that all team members must use the same IDE. However, this choice will direct where tight-integration investment will be prioritized. For example, if Visual Studio Code is the **suggested** IDE then, the team would focus on integrating VS code tasks and launch configurations over similar integrations for other IDEs. Team members should still feel free to use their preferred IDE as long as it does not negatively impact the team.

### DevEx Champion - Identify Iterative Improvements

The DevEx champion takes ownership in holding the team accountable for providing a positive developer experience. The following outline responsibilities for the DevEx champion.

- Actively seek opportunities for improving the solution developer experience
- Work with the Dev Lead to iteratively improve team expectations for developer experience

- Curate a backlog actionable stories that identify areas for improvement and prioritize with respect to project delivery goals by engaging directly with the Product Owner and Customer.
- Serve as subject-matter expert for the rest of the team. Help the team determine how to implement DevEx expectations and identify deviations.

### Team Members - Assert Expectations

The team members of the team can also help hold each other accountable for providing a positive developer experience. The following are examples of areas team members can help identify where the team's DevEx expectations are not being met.

- Pull requests. Try the changes locally to see if they are adhering to the team's DevEx expectations.
- Design Reviews. Look for proposals that may negatively affect the solution's DevEx. These might include
  - Introduction of new tech whose testability is limited to manual steps in a deployed environment.
  - Addition of new repository

### New Team Members - Identify Iterative Improvements

New team members are uniquely positioned to identify instances of undocumented [Collective Wisdom](https://en.wikipedia.org/wiki/Collective_wisdom). The following outlines responsibilities of new team members as it relates to DevEx:

- If you come across missing, incomplete or incorrect documentation while onboarding, you should record the issue as a new defect(s) and assign it to the product owner to triage.
- If no onboarding documentation exists, note the steps you took in a new user story. Assign the new story to the product owner to triage.

## Facilitation Guidance

The following outline examples of several strategies that can be adopted to promote a positive developer experience. It is expected that each team should define what a positive dev experience means within the context of their project. Additionally, refine that over time via feedback mechanisms such as sprint and project retrospectives.

### Establish Hotkeys

Assign hotkeys to each of the essential tasks.

| Task | Windows |
| --- | --- |
| Build | CTRL+SHIFT+B |
| Test | CTRL+R,T |
| Start With Debugging | F5 |

### The F5 Contract

The F5 contract aims for the ability to run the end-to-end solution with the following steps.

1. Clone - git clone \[ `my-repo-url-here`\]
2. Configure - set any configuration values that need to be unique to the individual (i.e. update a .env file)
3. Press F5 - launch the solution with debugging attached.

Most IDEs have some form of a task runner that can be used to automate the build, execute, and attach steps. Try to leverage these such that the steps can all be run with as few manual steps as possible.

### DevEx Champion Actively Seek Improvements

The DevEx champion should actively seek areas where the team has opportunity to improve. For example, do they need to deploy their changes to an environment off their laptop before they can validate if what they did worked. Rather than debugging locally, do they have to do this repetitively to get to a working solution? Does this take several minutes each iteration? Does this block other developers due to the contention on the environment?

The following are ceremonies that the DevEx champion can use to find potential opportunities

- Retrospectives. Is feedback being raised that relates to the essential tasks being difficult or unwieldy?
- Standup Blockers. Are individuals getting blocked or stumbling on the essential tasks?

As opportunities are identified, the DevEx champion can translate these into actionable stories for the product backlog.

### Make Tasks Cross Platform

For essential tasks being standardized during the engagement, ensure that different platforms are accounted for. Team members may have different operating systems and ensuring the tasks are cross-platform will provide an additional opportunity to improve the experience.

- See the [making tasks cross platform recipe](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/cross-platform-tasks/) for guidance on how tasks can be configured to include different platforms.

### Create an Onboarding Guide

When welcoming new team members to the engagement, there are many areas for them to get adjusted to and bring them up to speed including codebase, coding standards, team agreements, and team culture. By adopting a strong onboarding practice such as an onboarding guide in a centralized location that explains the scope of the project, processes, setup details, and software required, new members can have all the necessary resources for them to be efficient, successful and a valuable team member from the start.

See the [onboarding guide recipe](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/onboarding-guide-template/) for guidance on what an onboarding guide may look like.

### Standardize Essential Tasks

Apply a common strategy across solution components for performing the essential tasks

- Standardize the configuration for solution components
- Standardize the way tests are run for each component
- Standardize the way each component is started and stopped locally
- Standardize how to document the essential tasks for each component

This standardization will enable the team to more easily automate these tasks across all components at the solution level. See Solution-level Essential Tasks below.

### Solution-level Essential Tasks

Automate the ability to execute each essential task across all solution components. An example would be mapping the build action in the IDE to run the build task for each component in the solution. More importantly, configure the IDE start action to start all components within the solution. This will provide significant efficiency for the engineering team when dealing with multi-component solutions.

When this is not implemented, the engineers must repeat each of the essential tasks manually for each component in the solution. In this situation, the number of steps required to perform each essential task is multiplied by the number of components in the system

\[Configuration steps + Build steps + Start/Debug steps + Stop steps + Run test steps + Documenting all of the above\] \* \[many solution components\] = TOO MANY STEPS

VS.

\[Configuration steps + Build steps + Start/Debug steps + Stop steps + Run test steps + Documenting all of the above\] \* \[1 solution\] = MINIMUM NUMBER OF STEPS

### Observability

[Observability](https://microsoft.github.io/code-with-engineering-playbook/observability/) alleviates unforeseen challenges for the developer in a complex distributed system. It identifies project bottlenecks quicker and with more precision, enhancing performance as the developer seeks to deploy code changes. Adding observability improves the experience when identifying and resolving bugs or broken code. This results in fewer or less severe current and future production failures.

There are many observability strategies a developer can use alongside best engineering practices. These resources improve the DevEx by ensuring a shared view of the complex system throughout the entire lifecycle. Observability in code via logging, exception handling and exposing of relevant application metrics for example, promotes the consistent visibility of real time performance. The observability pillars, [logging](https://microsoft.github.io/code-with-engineering-playbook/observability/pillars/logging/), [metrics](https://microsoft.github.io/code-with-engineering-playbook/observability/pillars/metrics/), and [tracing](https://microsoft.github.io/code-with-engineering-playbook/observability/pillars/tracing/), detail when to enable each of the three specific types of observability.

### Minimize the Number of Repositories

Splitting a solution across multiple repositories can negatively impact the above measures. This can also negatively impact other areas such as Pull Requests, Automated Testing, Continuous Integration, and Continuous Delivery. Similar to the IDE instances, the negative impact is multiplied by the number of repositories.

\[Clone steps + Branching steps + Commit steps + CI steps + Pull Request reviews & merges \] \* \[many source code repositories\] = TOO MANY STEPS

VS.

\[Clone steps + Branching steps + Commit steps + CI steps + Pull Request reviews & merges \] \* \[1 source code repository\] = MINIMUM NUMBER OF STEPS

#### Atomic Pull Requests

When the solution is encapsulated within a single repository, it also allows pull requests to represent a change across multiple layers. This is especially helpful when a change requires changes to a shared contract between multiple components. For example, a story requires that an api endpoint is changed. With this strategy the api and web client could be updated with the same pull request. This avoids the main branch being broken temporarily while waiting on dependent pull requests to merge.

### Minimize Remote Dependencies for Local Development

The fewer dependencies on components that cannot run a developer's machine translate to fewer steps required to get started. Therefore, fewer dependencies will positively impact the measures above.

The following strategies can be used to reduce these dependencies

#### Use an Emulator

If available, emulators are implementations of technologies that are typically only available in cloud environments. A good example is the [CosmosDB emulator](https://learn.microsoft.com/en-us/azure/cosmos-db/local-emulator).

#### Use DI + Toggle to Mock Remote Dependencies

When the solution depends on a technology that cannot be run on a developer's machine, the setup and testing of that solution can be challenging. One strategy that can be employed is to create the ability to swap that dependency for one that can run locally.

Abstract the layer that has the remote dependency behind an interface owned by the solution (not the remote dependency). Create an implementation of that interface using a technology that can be run locally. Create a factory that decides which instance to use. This decision could be based on environment configuration (i.e. the toggle). Then, the original class that depends on the remote tech instead should depend on the factory to provide which instance to use.

Much of this strategy can be simplified with proper dependency injection technique and/or framework.

See example below that swaps Azure Service Bus implementation for RabbitMQ which can be run locally.

```
interface IPublisher {
    send(message: string): void
}
class RabbitMQPublisher implements IPublisher {
    send(message: string) {
        //todo: send the message via RabbitMQ
    }
}
class AzureServiceBusPublisher implements IPublisher {
    send(message: string) {
        //todo: send the message via Azure Service Bus
    }
}
interface IPublisherFactory{
    create(): IPublisher
}
class PublisherFactory{
    create(): IPublisher {
        // use env var value to determine which instance should be used
        if(process.env.UseAsb){
            return new AzureServiceBusPublisher();
        }
        else{
            return new RabbitMqPublisher();
        }
    }
}
class MyService {
    //inject the factory
    constructor(private readonly publisherFactory: IPublisherFactory){
    }
    sendAMessage(message: string): void{
        //use the factory to determine which instance to use
        const publisher: IPublisher = this.publisherFactory.create();
        publisher.send(message);
    }
}

```

The recipes section has a more complete discussion on [DI as part of a high productivity inner dev loop](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/client-app-inner-loop/)

* * *


Last update:
August 22, 2024[Skip to content](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/client-app-inner-loop/#separating-client-apps-from-the-services-they-consume-during-development)

# Separating Client Apps from the Services They Consume During Development

Client Apps typically rely on remote services to power their apps.
However, development schedules between the client app and the services don't always fully align. For a high velocity inner dev loop, client app development must be decoupled from the backend services while still allowing the app to "invoke" the services for local testing.

## Options

Several options exist to decouple client app development from the backend services. The options range from embedding mock implementation of the services into the application, others rely on simplified versions of the services.

This document lists several options and discusses trade-offs.

### Embedded Mocks

An embedded mock solution includes classes that implement the service interfaces locally. Interfaces and data classes, also called models or data transfer objects or DTOs, are often generated from the services' API specs using tools like nswag ( [RicoSuter/NSwag: The Swagger/OpenAPI toolchain for .NET, ASP.NET Core and TypeScript. (github.com)](https://github.com/RicoSuter/NSwag)) or autorest ( [Azure/autorest: OpenAPI (f.k.a Swagger) Specification code generator. Supports C#, PowerShell, Go, Java, Node.js, TypeScript, Python, Ruby (github.com)](https://github.com/Azure/AutoRest)).

A simple service implementation can return a static response. For RESTful services, the JSON responses for the stubs can be stored as application resources or simply as static strings.

```
public Task<UserProfile> GetUserAsync(long userId, CancellationToken cancellationToken)
{
    PetProfile result = Newtonsoft.Json.JsonConvert.DeserializeObject<UserProfile>(
        MockUserProfile.UserProfile, new Newtonsoft.Json.JsonSerializerSettings());

    return Task.FromResult(result);
}

```

More sophisticated can randomly return errors to test the app's resiliency code paths.

Mocks can be activated via conditional compilation or dynamically via app configuration. In either case, it is recommended to ensure that mocks, service responses and externalized configurations are not included in the final release to avoid confusing behavior and inclusion of potential vulnerabilities.

#### Sample: Registering Mocks via Dependency Injection

Dependency Injection Containers like Unity ( [Unity Container Introduction \| Unity Container](http://unitycontainer.org/articles/introduction.html)) make
it easy to switch between mock services and real service client implementations. Since both implement the same interface, implementations can be registered with the Unity container.

```
public static void Bootstrap(IUnityContainer container)
{

#if DEBUG
    container.RegisterSingleton<IUserServiceClient, MockUserService>();
#else
    container.RegisterSingleton<IUserServiceClient, UserServiceClient>();
#endif

}

```

#### Consuming Mocks via Dependency Injection

The code consuming the interfaces will not notice the difference.

```
public class UserPageModel
{
    private readonly IUserServiceClient userServiceClient;

    public UserPageModel(IUserServiceClient userServiceClient)
    {
        this.userServiceClient = userServiceClient;
    }

    // ...
}

```

### Local Services

The approach with Locally Running Services is to replace the call in the client from pointing to the actual endpoint (whether dev, QA, prod, etc.) to a local endpoint.

This approach also enables injecting traffic capture and shaping proxies like Postman ( [Postman API Platform \| Sign Up for Free](https://www.postman.com/)) or Fiddler ( [Fiddler \| Web Debugging Proxy and Troubleshooting Solutions (telerik.com)](https://www.telerik.com/fiddler)).

The advantage of this approach is that the APIs are decoupled from the client and can be independently updated/modified (e.g. changing response codes, changing data) without requiring changes to the client. This helps to unlock new development scenarios and provides flexibility during the development phase.

The challenge with this approach is that it does require setup, configuration, and running of the services locally. There are tools that help to simplify that process (e.g. [JsonServer](https://www.npmjs.com/package/json-server), [Postman Mock Server](https://learning.postman.com/docs/designing-and-developing-your-api/mocking-data/setting-up-mock/)).

#### High-Fidelity Local Services

A local service stub implements the expected APIs. Just like the embedded mock, it can be generated based on existing API contracts (e.g. OpenAPI).

A high-fidelity approach packages the real services together with simplified data in docker containers that can be run locally using docker-compose before the client app is started for local debugging and testing. To enable running services fully local the "local version" substitutes dependent cloud services with local alternatives, e.g. file storage instead of blobs, locally running SQL Server instead of SQL AzureDB.

This approach also enables full fidelity integration testing without spinning up distributed deployments.

### Stub / Fake Services

Lower fidelity approaches run stub services, that could be generated from API specs, or run fake servers like JsonServer ( [JsonServer.io: A fake json server API Service for prototyping and testing.](https://www.jsonserver.io/)) or Postman. All these services would respond with predetermined and configured JSON messages.

## How to Decide

|  | Pros | Cons | Example when developing for: | Example When not to Use |
| --- | --- | --- | --- | --- |
| Embedded Mocks | Simplifies the F5 developer experience | Tightly coupled with Client | More static type data scenarios | Testing (e.g. unit tests, integration tests) |
|  | No external dependencies to manage | Hard coded data | Initial integration with services |  |
|  |  | Mocking via Dependency Injection can be a non-trivial effort |  |  |
| High-Fidelity Local Services | Loosely Coupled from Client | Extra tooling required i.e. local infrastructure overhead | URL Routes | When API contract are not available |
|  | Easier to independently modify response | Extra setup and configuration of services |  |  |
|  | Independent updates to services |  |  |  |
|  | Can utilize HTTP traffic |  |  |  |
|  | Easier to replace with real services at a later time |  |  |  |
| Stub/Fake Services | Loosely coupled from client | Extra tooling required i.e. local infrastructure overhead | Response Codes | When API Contracts available |
|  | Easier to independently modify response | Extra setup and configuration of services | Complex/variable data scenarios | When API Contracts are note available |
|  | Independent updates to services | Might not provide full fidelity of expected API |  |  |
|  | Can utilize HTTP traffic |  |  |  |
|  | Easier to replace with real services at a later time |  |  |  |

* * *


Last update:
August 26, 2024[Skip to content](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/copilots/#copilots)

# Copilots

There are a number of AI tools that can improve the developer experience. This article will discuss tooling that is available as well as advice on when it might be appropriate to use such tooling.

## GitHub Copilot

The current version of GitHub Copilot can provide code completion in many popular IDEs. For instance, the [VS Code extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) that can be installed from the VS Code Marketplace. It requires a GitHub account to use. For more information about what IDEs are supported, what languages are supported, cost, features, etc., please checkout out the information on [Copilot](https://github.com/features/copilot) and [Copilot for Business](https://resources.github.com/copilot-for-business/).

Some example use-cases for GitHub Copilot include:

- **Write Documentation**. For example, the above paragraph was written using Copilot.

- **Write Unit Tests**. Given that setup and assertions are often consistent across unit tests, Copilot tends to be very accurate.

- **Unblock**. It is often hard start writing when staring at a blank page, Copilot can fill the space with something that may or may not be what you ultimately want to do, but it can help get you in the right head space.

If you want Copilot to write something useful for you, try writing a comment that describes what your code is going to do - it can often take it from there.

## GitHub Copilot Labs

Copilot has a [GitHub Copilot labs extension](https://githubnext.com/projects/copilot-labs/) that offers additional features that are not yet ready for prime-time. For VS Code, you can install it from the VS Code Marketplace. These features include:

- **Explain**. Copilot can explain what the code is doing in natural language.

- **Translate**. Copilot can translate code from one language to another.

- **Brushes**. You can select code that Copilot then modifies inline based on a "brush" you select, for example, to make the code more readable, fix bugs, improve debugging, document, etc.

- **Generate Tests**. Copilot can generate unit tests for your code. Though currently this is limited to JavaScript and TypeScript.

## GitHub Copilot X

The next version of Copilot offers a number of new use-cases beyond code completion. These include:

- **Chat**. Rather than just providing code completion, Copilot will be able to have a conversation with you about what you want to do. It has context about the code you are working on and can provide suggestions based on that context. Beyond just writing code, consider using chat to:

- **Build SQL Indexes**. Given a query, Copilot can generate a SQL index that will improve the performance of the query.

- **Write Regular Expressions**. These are notoriously difficult to write, but Copilot can generate them for you if you give some sample input and describe what you want to extract.

- **Improve and Validate**. If you are unsure of the implications of writing code a particular way, you can ask questions about it. For instance, you might ask if there is a way to write the code that is more performant or uses less memory. Once it gives you an opinion, you can ask it to provide documentation validating that assertion.

- **Explain**. Copilot can explain what the code is doing in natural language.

- **Write Code**. Given prompting by the developer it can write code that you can one-click deploy into existing or new files.

- **Debug**. Copilot can analyze your code and propose solutions to fix bugs.

It can do most of what Labs can do with "brushes" as "topics", but whereas Labs changes the code in your file, the chat functionality just shows what it would change in the window. However, there is also an "inline mode" for GitHub Copilot Chat that allows you to make changes to your code inline which does not have this same limitation.

## ChatGPT / Bing Chat

For coding, generic AI chat tools such as ChatGPT and Bing Chat are less useful, but they still have their place. GitHub Copilot will only answer "questions about coding" and it's interpretation of that rule can be a little restrictive. Some cases for using ChatGPT or Bing Chat include:

- **Write Documentation**. Copilot can write documentation, but using ChatGPT or Bing Chat, you can expand your documentation to include business information, use-cases, additional context, etc.

- **Change Perspective**. ChatGPT can impersonate a persona or even a system and answer questions from that perspective. For example, you can ask it to explain what a particular piece of code does from the perspective of a user. You might have ChatGPT imagine it is a database administrator and ask it to explain how to improve a particular query.

When using Bing Chat, experiment with modes, sometimes changing to Creative Mode can give the results you need.

## Prompt Engineering

Chat AI tools are only as good as the prompts you give them. The quality and appropriateness of the output can vary greatly depending on the prompt. In addition, many of these tools restrict the number of prompts you can send in a given amount of time. To learn more about prompt engineering, you might review some open source documentation [here](https://github.com/brexhq/prompt-engineering).

## Considerations

It is important when using AI tools to understand how the data (including private or commercial code) might be used by the system. Read more about how GitHub Copilot handles your data and code [here](https://resources.github.com/copilot-for-business/).

* * *


Last update:
March 15, 2024[Skip to content](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/cross-platform-tasks/#cross-platform-tasks)

# Cross Platform Tasks

There are several options to alleviate cross-platform compatibility issues.

- Running tasks in a container
- Using the tasks-system in VS Code which provides options to allow commands to be executed specific to an operating system.

## Docker or Container Based

Using containers as development machines allows developers to get started with minimal setup and abstracts the development environment from the host OS by having it run in a container.
DevContainers can also help in standardizing the local developer experience across the team.

The following are some good resources to get started with running tasks in DevContainers

- [Developing inside a container](https://code.visualstudio.com/docs/remote/containers).
- [Tutorial on Development in Containers](https://code.visualstudio.com/docs/remote/containers-tutorial)
- For samples projects and dev container templates see [VS Code Dev Containers Recipe](https://github.com/microsoft/vscode-dev-containers)
- [Dev Containers Library](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/devcontainers-getting-started/)

## Tasks in VSCode

### Running Node.js

The example below offers insight into running Node.js executable as a command with tasks.json and how it can be treated differently on Windows and Linux.

```
{
  "label": "Run Node",
  "type": "process",
  "windows": {
    "command": "C:\\Program Files\\nodejs\\node.exe"
  },
  "linux": {
    "command": "/usr/bin/node"
  }
}

```

In this example, to run Node.js, there is a specific windows command, and a specific linux command. This allows for platform specific properties. When these are defined, they will be used instead of the default properties when the command is executed on the Windows operating system or on Linux.

### Custom Tasks

Not all scripts or tasks can be auto-detected in the workspace. It may be necessary at times to defined your own custom tasks. In this example, we have a script to run in order to set up some environment correctly. The script is stored in a folder inside your workspace and named test.sh for Linux & macOS and test.cmd for Windows. With the tasks.json file, the execution of this script can be made possible with a custom task that defines what to do on different operating systems.

```
{
  "version": "2.0.0",
  "tasks": [\
    {\
      "label": "Run tests",\
      "type": "shell",\
      "command": "./scripts/test.sh",\
      "windows": {\
        "command": ".\\scripts\\test.cmd"\
      },\
      "group": "test",\
      "presentation": {\
        "reveal": "always",\
        "panel": "new"\
      }\
    }\
  ]
}

```

The command here is a shell command and tells the system to run either the test.sh or test.cmd. By default, it will run test.sh with that given path. This example here also defines Windows specific properties and tells it execute test.cmd instead of the default.

### Resources

VS Code Docs - [operating system specific properties](https://vscode-docs.readthedocs.io/en/stable/editor/tasks/#operating-system-specific-properties)

* * *


Last update:
August 26, 2024[Skip to content](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/devcontainers-getting-started/#dev-containers-getting-started)

# Dev Containers: Getting Started

If you are a developer and have experience with Visual Studio Code (VS Code) or Docker, then it's probably time you look at [development containers](https://code.visualstudio.com/docs/remote/containers) (dev containers). This readme is intended to assist developers in the decision-making process needed to build dev containers. The guidance provided should be especially helpful if you are experiencing VS Code dev containers for the first time.

> **Note:** This guide is not about setting up a Docker file for deploying a running Python program for CI/CD.

## Prerequisites

- Experience with VS Code
- Experience with Docker

## What are Dev Containers?

Development containers are a VS Code feature that allows developers to package a local development tool stack into the internals of a Docker container while also bringing the VS Code UI experience with them. Have you ever set a breakpoint inside a Docker container? Maybe not. Dev containers make that possible. This is all made possible through a VS Code extension called the [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) that works together with Docker to spin-up a VS Code Server within a Docker container. The VS Code UI component remains local, but your working files are volume mounted into the container. The diagram below, taken directly from the [official VS Code docs](https://code.visualstudio.com/docs/remote/containers), illustrates this:

![image](https://user-images.githubusercontent.com/10041279/93239062-e1b9a480-f747-11ea-94fb-3d50b14fd9b1.png)

If the above diagram is not clear, a basic analogy that might help you intuitively understand dev containers is to think of them as a union between Docker's interactive mode ( `docker exec -it 987654e0ff32`), and the VS Code UI experience that you are used to.

To set yourself up for the dev container experience described above, use your VS Code's Extension Marketplace to install the [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).

## How can Dev Containers Improve Project Collaboration?

VS Code dev containers have improved project collaboration between developers on recent team projects by addressing two very specific problems:

- Inconsistent local developer experiences within a team.
- Slow onboarding of developers joining a project.

The problems listed above were addressed by configuring and then sharing a dev container definition. Dev containers are defined by their base image, and the artifacts that support that base image. The base image and the artifacts that come with it live in the .devcontainer directory. This directory is where configuration begins. A central artifact to the dev container definition is a configuration file called `devcontainer.json`. This file orchestrates the artifacts needed to support the base image and the dev container lifecycle. Installation of the [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) is required to enable this orchestration within a project repo.

All developers on the team are expected to share and use the dev container definition (.devcontainer directory) in order to spin-up a container. This definition provides consistent tooling for locally developing an application across a team.

The code snippets below demonstrate the common location of a .devcontainer directory and devcontainer.json file within a project repository. They also highlight the correct way to reference a Docker file.

```
$ tree vs-code-remote-try-python  # main repo directory
└───.devcontainers
        ├───Dockerfile
        ├───devcontainer.json

```

```
# devcontainer.json
{
    "name": "Python 3",
    "build": {
        "dockerfile": "Dockerfile",
        "context": "..",
        // Update 'VARIANT' to pick a Python version: 3, 3.6, 3.7, 3.8
        "args": {"VARIANT": "3.8"}
    },
}

```

For a list of devcontainer.json configuration properties, visit VS Code documentation on [dev container properties](https://code.visualstudio.com/docs/remote/devcontainerjson-reference).

## How do I Decide Which Dev Container is Right for my Use Case?

Fortunately, VS Code has a repo gallery of platform specific folders that host dev container definitions (.devcontainer directories) to make getting started with dev containers easier. The code snippet below shows a list of gallery folders that come directly from the [VS Code dev container gallery repo](https://github.com/microsoft/vscode-dev-containers/tree/master/containers):

```
$ tree vs-code-dev-containers  # main repo directory
└───containers
        ├───dotnetcore
        |   └───.devcontainers # dev container
        ├───python-3
        |   └───.devcontainers # dev container
        ├───ubuntu
        |   └───.devcontainers # dev container
        └───....

```

Here are the final high-level steps it takes to build a dev container:

1. Decide which platform you'd like to build a local development tool stack around.
2. Browse the VS Code provided dev container gallery of project folders that target your platform and choose the most appropriate one.
3. Inspect the dev container definitions (.devcontainer directory) of a project for the base image, and the artifacts that support that base image.
4. Use what you've discovered to begin setting up the dev container as it is, extending it or building your own from scratch.

## Going further

There are use cases where you would want to go further in configuring your Dev Container. [More details here](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/devcontainers-going-further/)

* * *


Last update:
August 26, 2024[Skip to content](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/devcontainers-going-further/#dev-containers-going-further)

# Dev Containers: Going further

Dev Containers allow developers to share a common working environment, ensuring that the runtime and all dependencies versions are consistent for all developers.

Dev containers also allow us to:

1. Leverage existing tools to enhance the Dev Containers with more features,
2. Provide custom tools (such as scripts) for other developers.

## Existing tools

In the development phase, you will most probably need to use tools not installed by default in your Dev Container. For instance, if your project's target is to be deployed on Azure, you will need [Azure-cli](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) and maybe [Terraform](https://www.terraform.io/) for resources and application deployment. You can find such Dev Containers in the [VS Code dev container gallery repo](https://github.com/devcontainers/templates/tree/main/src).

Some other tools may be:

- Linters for [markdown](https://github.com/DavidAnson/markdownlint) files,
- Linters for [bash](https://www.shellcheck.net/) scripts,
- Etc...

Linting files that are not _the source code_ can ensure a common format with common rules for each developer. These checks should be also run in a [Continuous Integration Pipeline](https://learn.microsoft.com/azure/devops/pipelines/architectures/devops-pipelines-baseline-architecture), but it is a good practice to run them prior opening a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

## Limitation of custom tools

If you decide to include [Azure-cli](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) in your Dev Container, developers will be able to run commands against their tenant. However, to make the developers' lives easier, we could go further by letting them prefill their connection information, such as the `tenant ID` and the `subscription ID` in a secure and persistent way (do not forget that your Dev Container, being a [Docker](https://www.docker.com/) container, might get deleted, or the image could be rebuilt, hence, all customization _inside_ will be lost).

One way to achieve this is to leverage environment variables, with untracked `.env` file part of the solution being injected in the Dev Container.

Consider the following files structure:

```
My Application  # main repo directory
└───.devcontainer
|       ├───Dockerfile
|       ├───devcontainer.json
└───config
|       ├───.env
|       ├───.env-sample

```

The file `config/.env-sample` is a tracked file where anyone can find environment variables to set (with no values, obviously):

```
TENANT_ID=
SUBSCRIPTION_ID=

```

Then, each developer who clones the repository can create the file `config/.env` and fills it in with the appropriate values.

In order now to inject the `.env` file into the container, you can update the file `devcontainer.json` with the following:

```
{
    ...
    "runArgs": ["--env-file","config/.env"],
    ...
}

```

As soon as the Dev Container is started, these environment variables are sent to the container.

Another approach would be to use Docker Compose, a little bit more complex, and probably _too much_ for just environment variables. Using Docker Compose can unlock other settings such as custom dns, ports forwarding or multiple containers.

To achieve this, you need to add a file `.devcontainer/docker-compose.yml` with the following:

```
version: '3'
services:
  my-workspace:
    env_file: ../config/.env
    build:
      context: .
      dockerfile: Dockerfile
    command: sleep infinity

```

To use the `docker-compose.yml` file instead of `Dockerfile`, we need to adjust `devcontainer.json` with:

```
{
    "name": "My Application",
    "dockerComposeFile": ["docker-compose.yml"],
    "service": "my-workspace"
    ...
}

```

This approach can be applied for many other tools by preparing what would be required. The idea is to simplify developers' lives and new developers joining the project.

## Custom tools

While working on a project, any developer might end up writing a script to automate a task. This script can be in `bash`, `python` or whatever scripting language they are comfortable with.

Let's say you want to ensure that all markdown files written are validated against specific rules you have set up. As we have seen above, you can include the tool [markdownlint](https://github.com/DavidAnson/markdownlint) in your Dev Container . Having the tool installed does not mean developer will know how to use it!

Consider the following solution structure:

```
My Application  # main repo directory
└───.devcontainer
|       ├───Dockerfile
|       ├───docker-compose.yml
|       ├───devcontainer.json
└───scripts
|       ├───check-markdown.sh
└───.markdownlint.json

```

The file `.devcontainer/Dockerfile` installs [markdownlint](https://github.com/DavidAnson/markdownlint)

```
...
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y nodejs npm

# Add NodeJS tools
RUN npm install -g markdownlint-cli
...

```

The file `.markdownlint.json` contains the rules you want to validate in your markdown files (please refer to the [markdownlint site](https://github.com/DavidAnson/markdownlint) for details).

And finally, the script `scripts/check-markdown.sh` contains the following code to execute `markdownlint`:

```
# Get the repository root
repoRoot="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." >/dev/null 2>&1 && pwd )"

# Execute markdownlint for the entire solution
markdownlint -c "${repoRoot}"/.markdownlint.json

```

When the Dev Container is loaded, any developer can now run this script in their terminal:

```
/> ./scripts/check-markdown.sh

```

This is a small use case, there are unlimited other possibilities to capitalize on work done by developers to save time.

## Other considerations

### Platform architecture

When installing tooling, you also need to ensure that you know what host computers developers are using. All Intel based computers, whether they are running Windows, Linux or MacOs will have the same behavior.
However, the latest Mac architecture (Apple M1/Silicon) being ARM64, means that the behavior is not the same when building Dev Containers.

For instance, if you want to install [Azure-cli](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) in your Dev Container, you won't be able to do it the same way you do it for Intel based machines. On Intel based computers you can install the `deb` package. However, this package is not available on ARM architecture. The only way to install [Azure-cli](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) on Linux ARM is via the Python installer `pip`.

To achieve this you need to check the architecture of the host building the Dev Container, either in the Dockerfile, or by calling an external bash script to install remaining tools not having a universal version.

Here is a snippet to call from the Dockerfile:

```
# If Intel based, then use the deb file
if [[ `dpkg --print-architecture` == "amd64" ]]; then
    sudo curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash;
else
# arm based, install pip (and gcc) then azure-cli
    sudo apt-get -y install gcc
    python3 -m pip install --upgrade pip
    python3 -m pip install azure-cli
fi

```

### Reuse of credentials for GitHub

If you develop inside a Dev Container, you will also want to share your GitHub credentials between your host and the Dev Container. Doing so, you would avoid copying your ssh keys back and forth (if you are using ssh to access your repositories).

One approach would be to mount your local `~/.ssh` folder into your Dev Container. You can either use the `mounts` option of the `devcontainer.json`, or use Docker Compose

- Using `mounts`:

```
{
    ...
    "mounts": ["source=${localEnv:HOME}/.ssh,target=/home/vscode/.ssh,type=bind"],
    ...
}

```

As you can see, `${localEnv:HOME}` returns the host `home` folder, and it maps it to the container `home` folder.

- Using Docker Compose:

```
version: '3'
services:
  my-worspace:
    env_file: ../configs/.env
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - "~/.ssh:/home/alex/.ssh"
    command: sleep infinity

```

Please note that using Docker Compose requires to edit the `devcontainer.json` file as we have seen above.

You can now access GitHub using the same credentials as your host machine, without worrying of persistence.

### Allow some customization

As a final note, it is also interesting to leave developers some flexibility in their environment for customization.

For instance, one might want to add aliases to their environment. However, changing the `~/.bashrc` file in the Dev Container is not a good approach as the container might be destroyed. There are numerous ways to set persistence, here is one approach.

Consider the following solution structure:

```
My Application  # main repo directory
└───.devcontainer
|       ├───Dockerfile
|       ├───docker-compose.yml
|       ├───devcontainer.json
└───me
|       ├───bashrc_extension

```

The folder `me` is untracked in the repository, leaving developers the flexibility to add personal resources. One of these resources can be a `.bashrc` extension containing customization. For instance:

```
# Sample alias
alias gaa="git add --all"

```

We can now adapt our `Dockerfile` to load these changes when the Docker image is built (and of course, do nothing if there is no file):

```
...
RUN echo "[ -f PATH_TO_WORKSPACE/me/bashrc_extension ] && . PATH_TO_WORKSPACE/me/bashrc_extension" >> ~/.bashrc;
...

```

* * *


Last update:
August 22, 2024[Skip to content](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/execute-local-pipeline-with-docker/#executing-pipelines-locally)

# Executing Pipelines Locally

## Abstract

Having the ability to execute pipeline activities locally has been identified as an opportunity to promote positive developer experience.
In this document we will explore a solution which will allow us to have the local CI experience to be as similar as possible to the remote process in the CI server.

Using the suggested method will allow us to:

- Build
- Lint
- Unit test
- E2E test
- Run Solution
- Be OS and environment agnostic.

## Enter Docker Compose

[Docker Compose](https://docs.docker.com/compose/) allows you to build push or run multi-container Docker applications.

### Method of Work

1. Dockerize your application(s), including a build step if possible.
2. Add a step in your docker file to execute unit tests.
3. Add a step in the docker file for linting.
4. Create a new dockerfile, possibly in a different folder, which executes end-to-end tests against the cluster. Make sure the default endpoints are configurable (This will become handy in your remote CI server, where you will be able to test against a live environment, if you choose to).
5. Create a docker-compose file which allows you to choose which of the services to run. The default will run all applications and tests, and an optional parameter can run specific services, for example only the application without the tests.

### Prerequisites

1. [Docker](https://www.docker.com/products/docker-desktop)
2. Optional: if you clone the sample app, you need to have [dotnet core](https://dotnet.microsoft.com/download) installed.

### Step by Step with Examples

For this tutorial we are going to use a [sample dotnet core api application](https://github.com/itye-msft/cse-engagement-template).
Here is the docker file for the sample app:

```
# https://hub.docker.com/_/microsoft-dotnet
FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /app

# copy csproj and restore as distinct layers
COPY ./ ./
RUN dotnet restore

RUN dotnet test

# copy everything else and build app
COPY SampleApp/. ./
RUN dotnet publish -c release -o out --no-restore

# final stage/image
FROM mcr.microsoft.com/dotnet/aspnet:5.0
WORKDIR /app
COPY --from=build /app/out .
ENTRYPOINT ["dotnet", "SampleNetApi.dll"]

```

This script restores all dependencies, builds and runs tests. The dotnet app includes `stylecop` which fails the build in case of linting issues.

Next we will also create a dockerfile to perform an end-to-end test. Usually this will look like a set of scripts, or a dedicated app which performs actual HTTP calls to a running application.
For the sake of simplicity the dockerfile itself will run a simple curl command:

```
FROM alpine:3.7
RUN apk --no-cache add curl
ENTRYPOINT ["curl","0.0.0.0:8080/weatherforecast"]

```

Now we are ready to combine both of the dockerfiles in a docker-compose script:

```
version: '3'
services:
  app:
    image: app:0.01
    build:
      context: .
    ports:
      - "8080:80"
  e2e:
    image: e2e:0.01
    build:
      context: ./E2E

```

The docker-compose script will launch the 2 dockerfiles, and it will build them if they were not built before.
The following command will run docker compose:

```
docker-compose up --build -d

```

Once the images are up, you can make calls to the service. The e2e image will perform the set of e2e tests.
If you want to skip the tests, you can simply tell compose to run a specific service by appending the name of the service, as follows:

```
docker-compose up --build -d app

```

Now you have a local script which builds and tests you application.
The next step would be make your CI run the docker-compose script.

Here is an example of a yaml file used by Azure DevOps pipelines:

```
trigger:
- master

pool:
  vmImage: 'ubuntu-latest'

variables:
  solution: '**/*.sln'
  buildPlatform: 'Any CPU'
  buildConfiguration: 'Release'

steps:
- task: DockerCompose@0
  displayName: Build, Test, E2E
  inputs:
    action: Run services
    dockerComposeFile: docker-compose.yml
- script: dotnet restore SampleApp
- script: dotnet build --configuration $(buildConfiguration) SampleApp
  displayName: 'dotnet build $(buildConfiguration)'

```

In this script the first step is docker-compose, which uses the same file we created the previous steps.
The next steps, do the same using scripts, and are here for comparison.
By the end of this step, your CI effectively runs the same build and test commands you run locally.

* * *


Last update:
August 22, 2024[Skip to content](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/fake-services-inner-loop/#fake-services-inner-dev-loop)

# Fake Services Inner Dev Loop

## Introduction

Consumers of remote services often find that their development cycle is not in sync with development of remote services, leaving developers of these consumers waiting for the remote services to "catch up". One approach to mitigate this issue and improve the inner dev loop is by decoupling and using Mock Services. Various Mock Service options are detailed [here](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/client-app-inner-loop/).

This document will focus on providing an example using the Fake Services approach.

## API

For our example API, we will work against a `/User` endpoint and the properties for `User` will be:

1. id - int
2. username - string
3. firstName - string
4. lastName - string
5. email - string
6. password - string
7. phone - string
8. userStatus - int

## Tooling

For the Fake Service approach, we will be using [Json-Server](https://github.com/typicode/json-server). Json-Server is a tool that provides the ability to fully fake REST APIs and run the server locally. It is designed to spin up REST APIs with CRUD functionality with minimal setup. Json-Server requires NodeJS and is installed via NPM.

```
npm install -g json-server

```

## Setup

In order to run Json-Server, it simply requires a source for data and will infer routes, etc. based on the data file. Note that additional customization can be performed for more advanced scenarios (e.g. custom routes). Details can be found [here](https://github.com/typicode/json-server#add-custom-routes).

For our example, we will use the following data file, `db.json`:

```
{
  "user": [\
    {\
      "id": 0,\
      "username": "user1",\
      "firstName": "Kobe",\
      "lastName": "Bryant",\
      "email": "kobe@example.com",\
      "password": "superSecure1",\
      "phone": "(123) 123-1234",\
      "userStatus": 0\
    },\
    {\
      "id": 1,\
      "username": "user2",\
      "firstName": "Shaquille",\
      "lastName": "O'Neal",\
      "email": "shaq@example.com",\
      "password": "superSecure2",\
      "phone": "(123) 123-1235",\
      "userStatus": 0\
    }\
  ]
}

```

## Run

Running Json-Server can be performed by simply running:

```
json-server --watch src/db.json

```

Once running, the User endpoint can be hit on the default localhost port: `http:/localhost:3000/user`

Note that Json-Server can be configured to use other ports using the following syntax:

```
json-server --watch db.json --port 3004

```

## Endpoint

The endpoint can be tested by running curl against it and we can narrow down which user object to get back with the following command:

```
curl http://localhost:3000/user/1

```

which, as expected, returns:

```
{
  "id": 1,
  "username": "user2",
  "firstName": "Shaquille",
  "lastName": "O'Neal",
  "email": "shaq@example.com",
  "password": "superSecure2",
  "phone": "(123) 123-1235",
  "userStatus": 0
}

```

* * *


Last update:
August 26, 2024[Skip to content](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/onboarding-guide-template/#onboarding-guide-template)

# Onboarding Guide Template

When developing an onboarding document for a team, it should contain details of engagement scope, team processes, codebase, coding standards, team agreements, software requirements and setup details. The onboarding guide can be used as an index to project specific content if it already exists elsewhere. Allowing this guide to be utilized as a foundation with the links will help keep the guide concise and effective.

## Overview and Goals

- List a few sentences explaining the high-level summary and the scope of the engagement.
- Consider adding any additional background and context as needed.
- Include the value proposition of the project, goals, what success looks like, and what the team is trying to achieve and why.

## Contacts

- List a few of the main contacts for the team and project overall such as the Dev Lead and Product Owner.
- Consider including the roles of these main contacts so that the team knows who to reach out to depending on the situation.

## Team Agreement and Code of Conduct

- Include the team's code of conduct or agreement that defines a set of expectation from each team member and how the team has agreed to operate.
- Working Agreement Template - [working agreement](https://microsoft.github.io/code-with-engineering-playbook/agile-development/team-agreements/working-agreement/)

## Dev Environment Setup

- Consider adding steps to run the project end-to-end. This could be in form of a separate wiki page or document that can be linked here.
- Include any software that needs to be downloaded and specify if a specific version of the software is needed.

## Project Building Blocks

- This can include a more in depth description with different areas of the project to help increase the project understanding.
- It can include different sections on the various components of the project including deployment, e2e testing, repositories.

## Resources

- This can include any additional links to documents related to the project
- It may include links to backlog items, work items, wiki pages or project history.

* * *


Last update:
August 26, 2024[Skip to content](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/toggle-vnet-dev-environment/#toggle-vnet-on-and-off-for-production-and-development-environment)

# Toggle VNet On and Off for Production and Development Environment

## Problem Statement

When deploying resources on Azure in a secure environment, resources are usually created behind a Private Network (VNet), without public access and with private endpoints to consume resources. This is the recommended approach for pre-production or production environments.

Accessing protected resources from a local machine implies one of the following options:

- Use a VPN
- Use a **jump box**
  - With SSH activated (less secure)
  - [With Bastion (recommended approach)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/cloud-scale-analytics/architectures/connect-to-environments-privately#about-azure-bastion-host-and-jumpboxes)

However, a developer may want to deploy a test environment (in a non-production subscription) for their tests during development phase, without the complexity of networking.

In addition, infrastructure code should not be duplicated: it has to be the same whether resources are deployed in a production like environment or in development environment.

## Option

The idea is to offer, **via a single boolean variable**, the option to deploy resources behind a VNet or not using one infrastructure code base. Securing resources behind a VNet usually implies that public accesses are disabled and private endpoints are created. This is something to have in mind because, as a developer, public access must be activated in order to connect to this environment.

The deployment pipeline will set these resources behind a VNet and will secure them by removing public accesses. Developers will be able to run the same deployment script, specifying that resources will not be behind a VNet nor have public accesses disabled.

Let's consider the following use case: we want to deploy a VNet, a subnet, a storage account with no public access and a private endpoint for the table.

The _magic_ variable that will help toggling security will be called `behind_vnet`, of type boolean.

Let's implement this use case using `Terraform`.

> The code below does not contain everything, the purpose is to show the pattern and not how to deploy these resources. For more information on Terraform, please refer to the [official documentation](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs).

There is no `if` _per se_ in Terraform to define whether a specific resource should be deployed or not based on a variable value. However, we can use the [`count`](https://developer.hashicorp.com/terraform/language/meta-arguments/count) meta-argument. The strength of this meta-argument is if its value is `0`, the block is skipped.

Here is below the code snippets for this deployment:

- variables.tf


```
variable "behind_vnet" {
      type    = bool
}

```


- main.tf


```
resource "azurerm_virtual_network" "vnet" {
      count = var.behind_vnet ? 1 : 0

      name                = "MyVnet"
      address_space       = [x.x.x.x/16]
      resource_group_name = "MyResourceGroup"
      location            = "WestEurope"

      ...

      subnet {
          name              = "subnet_1"
          address_prefix    = "x.x.x.x/24"
      }
}

resource "azurerm_storage_account" "storage_account" {
      name                = "storage"
      resource_group_name = "MyResourceGroup"
      location            = "WestEurope"
      tags                = var.tags

      ...

      public_network_access_enabled = var.behind_vnet ? false : true
}

resource "azurerm_private_endpoint" "storage_account_table_private_endpoint" {
      count = var.behind_vnet ? 1 : 0

      name                = "pe-storage"
      subnet_id           = azurerm_virtual_network.vnet[0].subnet[0].id

      ...

      private_service_connection {
          name                           = "psc-storage"
          private_connection_resource_id = azurerm_storage_account.storage_account.id
          subresource_names              = [ "table" ]
          ...
      }

      private_dns_zone_group {
          name = "privateDnsZoneGroup"
          ...
      }
}

```


If we run

```
terraform apply -var behind_vnet=true

```

then all the resources above will be deployed, and it is what we want on a pre-production or production environment. The instruction `count = var.behind_vnet ? 1 : 0` will set `count` with the value `1`, therefore blocks will be executed.

However, if we run

```
terraform apply -var behind_vnet=false

```

the `azurerm_virtual_network` and `azurerm_private_endpoint` resources will be skipped (because `count` will be `0`). The resource `azurerm_storage_account` will be created, with minor differences in some properties: for instance, here, `public_network_access_enabled` will be set to `true` (and this is the goal for a developer to be able to access resources created).

The same pattern can be applied over and over for the entire infrastructure code.

## Conclusion

With this approach, the same infrastructure code base can be used to target a production like environment with secured resources behind a VNet with no public accesses and also a more permissive development environment.

However, there are a couple of trade-offs with this approach:

- if a resource has the `count` argument, it needs to be treated as a list, and not a single item. In the example above, if there is a need to reference the resource `azurerm_virtual_network` later in the code,


```
azurerm_virtual_network.vnet.id

```



will not work. The following must be used



```
azurerm_virtual_network.vnet[0].id # First (and only) item of the collection

```


- The meta-argument `count` cannot be used with `for_each` for a whole block. That means that the use of loops to deploy multiple endpoints for instance will not work. Each private endpoints will need to be deployed individually.

* * *


Last update:
August 22, 2024
