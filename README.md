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

+\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\--+
\| ID \| Pull Request Title \| State \|
+\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\--+
\| 50159 \| fix: Updated postinstall to include config setup + updated
doc \| open \| \| 50156 \| feat(client): remove extra if statement in
the navigation header \| open \| \| 50144 \| fix(deps): update prisma
monorepo to v4.13.0 \| open \| \| 50142 \| docs: fix typos \| open \| \|
50132 \| fix: improvement in Use \@if and \@else to Add Logic To Your
Styles module \| open \| \| 50128 \| fix: typo in Target the Parent of
an Element Using jQuery module \| open \| \| 50125 \| fix: use onRequest
to add headers \| open \| \| 50120 \| feat(api): add CORS headers \|
open \| \| 50119 \| refactor(client): split lower-jaw to separate files
\| open \| \| 50117 \| feat(client): add react suspense and lazy loading
\| open \| \| 50110 \| fix(client): Prevent saving invalid portfolio
item \| open \| \| 50106 \| feat(client): use showPoints to hide points
instead of mutating the points \| open \| \| 50105 \| feat(client):
children for spacer component \| open \| \| 50099 \| test(api): allow
mocking of env vars \| open \| \| 50094 \| feat(client): Customized
Radio Buttons in settings page \| open \| \| 50093 \| feat(client):Weird
validation for portfolio inputs in the setting page \| open \| \| 50088
\| feat: replace code lock epic with saga \| open \| \| 50087 \| fix:
updated reset and help buttons \| open \| \| 50084 \| feat(client):
expose the language button to the navbar \| open \|
+\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\--+

Thanks and Regards,

Abhijeet Hapase
