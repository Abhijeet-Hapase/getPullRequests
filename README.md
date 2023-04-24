<p style='text-align: left;'> 
How to create Docker Image and run it:

1\) Please download below files uploaded into this repository.<br>  
  1.getPullRequests.py 2.Dockerfile 3.requirements.txt

2\) Please run following command to create docker image. <br>
  docker build --tag getpullrequests:1.0.1 .

3\) To list the image you have created in step 2,please run below
command.<br> 
  docker images

Output will be similar to below snip:

REPOSITORY TAG IMAGE ID CREATED SIZE<br> 
  getpullrequests 1.0.1 6d27e423dfaf
3 minutes ago 139MB <br>getpullrequests latest 9399b8799d60 2 hours ago
139MB <br>getpulrequests latest 9399b8799d60 2 hours ago 139MB 
4\) Docker
image created in step 3 takes 3 arguments:<br>  1. Repository Owner Name 2.
Repository Name 3. State of pull requests(open/closed/all).

To run the docker image with tag 1.0.1,execute below command:<br> docker run
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
| ID                                                                                                                                                                      | Pull Request Title                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | State                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 50159<br>50156<br>50144<br>50142<br>50132<br>50128<br>50125<br>50120<br>50119<br>50117<br>50110<br>50106<br>50105<br>50099<br>50094<br>50093<br>50088<br>50087<br>50084 | fix: Updated postinstall to include config setup + updated doc<br>feat(client): remove extra if statement in the navigation header<br>fix(deps): update prisma monorepo to v4.13.0<br>docs: fix typos<br>fix: improvement in Use @if and @else to Add Logic To Your Styles module<br>fix: typo in Target the Parent of an Element Using jQuery module<br>fix: use onRequest to add headers<br>feat(api): add CORS headers<br>refactor(client): split lower-jaw to separate files<br>feat(client): add react suspense and lazy loading<br>fix(client): Prevent saving invalid portfolio item<br>feat(client): use showPoints to hide points instead of mutating the points<br>feat(client): children for spacer component<br>test(api): allow mocking of env vars<br>feat(client): Customized Radio Buttons in settings page<br>feat(client):Weird validation for portfolio inputs in the setting page<br>feat: replace code lock epic with saga<br>fix: updated reset and help buttons<br>feat(client): expose the language button to the navbar | open<br>open<br>open<br>open<br>open<br>open<br>open<br>open<br>open<br>open<br>open<br>open<br>open<br>open<br>open<br>open<br>open<br>open<br>open |

Thanks and Regards,

Abhijeet Hapase
</p>
