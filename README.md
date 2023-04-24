How to create Docker Image and run it:

1\) Please download below files uploaded into this repository.  1.
getPullRequests.py 2.Dockerfile 3.requirements.txt

2\) Please run following command to create docker image. docker build
\--tag getpullrequests:1.0.1 .

3\) To list the image you have created in step 2,please run below
command. docker images

Output will be similar to below snip:

REPOSITORY TAG IMAGE ID CREATED SIZE getpullrequests 1.0.1 6d27e423dfaf
3 minutes ago 139MB getpullrequests latest 9399b8799d60 2 hours ago
139MB getpulrequests latest 9399b8799d60 2 hours ago 139MB 4) Docker
image created in step 3 takes 3 arguments:  1. Repository Owner Name 2.
Repository Name 3. State of pull requests(open/closed/all).

To run the docker image with tag 1.0.1,execute below command: docker run
getpullrequests:1.0.1 freeCodeCamp freeCodeCamp open

This should produce email format that will be sent to target audience as
below:

From: getpullrequestdata@noreply.com

To:jon.smith@test.com;alex.hewitt@test.com;scarlett.wilde@test.com;carl.ward@test.com

Subject: Pull Request Status : open

Hello,

Please see below status of pull requests from last week for repository:
freeCodeCamp

Number of Pull Requests : 19

Pull Request Details:

| ID                                                                                                                	| Pull Request Title                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         	| State                                                                                          	|
|-------------------------------------------------------------------------------------------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|------------------------------------------------------------------------------------------------	|
| 50159 50156 50144 50142 50132 50128 50125 50120 50119 50117 50110 50106 50105 50099 50094 50093 50088 50087 50084 	| fix: Updated postinstall to include config setup + updated doc feat(client): remove extra if statement in the navigation header fix(deps): update prisma monorepo to v4.13.0 docs: fix typos fix: improvement in Use @if and @else to Add Logic To Your Styles module fix: typo in Target the Parent of an Element Using jQuery module fix: use onRequest to add headers feat(api): add CORS headers refactor(client): split lower-jaw to separate files feat(client): add react suspense and lazy loading fix(client): Prevent saving invalid portfolio item feat(client): use showPoints to hide points instead of mutating the points feat(client): children for spacer component test(api): allow mocking of env vars feat(client): Customized Radio Buttons in settings page feat(client):Weird validation for portfolio inputs in the setting page feat: replace code lock epic with saga fix: updated reset and help buttons feat(client): expose the language button to the navbar 	| open open open open open open open open open open open open open open open open open open open 	|
Thanks and Regards,

Abhijeet Hapase
