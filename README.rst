beat\drift\-cli
+==============-

A Command Line Interface (CLI) that can be used to detect infrastructural drift (differences) between AWS service resources and Infrastructure As Code (IaC) environment states on IaC platform Terraform.

Please note that this tool was adapted from the "aws_list_all" library package

List all resources in a configured AWS account, including all regions, and services(*) with the options to writes JSON files for further use, which can be stored in the directory entered and used to compare with a possible list terraform resources to identify differences and inform the user of  the infrastructural drift identified.

(*) No guarantees for completeness. Use billing alerts if you are worried about costs.

.. image:: https://img.shields.io/badge/pypi-v0.0.1-blue
   :alt: PyPI

Usage
-----

You need to have python (both 2 or 3 work) as well as AWS credentials set up as usual.

Once the environment is set up correctly; cd into the “BeatDrift-CLI” folder via the command line to execute the python scripts; 
Please enter :
chmod +x __main__.py

Then :
cp __main__.py ~/bin/beatdrift-cli-master

The user would then be able to run the program using commands such as:
beatdrift-cli query --region us-east-1 --service ec2 --directory ./listdataCheck2/



However, since full integration was not achieved in the project, if the user is having problems with the execution or have prompts about missing modules, you can utilize the ‘aws-list-all’ package incorporated by BeatDrift-cli (with credit given in the notice to the author) to achieve the same results of crawling AWS resources and storing them as json files within the designated directory/folder within the project’s  folder.


AWS resources can be crawled by installing and using the “aws-list-all” package by entering the commands:

(Check the path of whichever python version you are using and also the path of the aws cli) I.e::


(which python3) aws


Then enter was to check if you have the was cli 

aws


Then::

pip install aws-list-all


After installation in the user's chosen directory, the user is able 'cd' into the directory of choice to query specific AWS resources by typing in the following::

cd /directoryOFChoice ::

$ cd /beatdrift-cli

Then enter


aws_list_all query --region us-east-1 --service ec2 --directory ./list_data/

So input will look like, please note that "beatdrift-cli$" represents the name of the project directory we are in, and not part of the commands at this stage of integration::


beatdrift-cli$  aws_list_all query --region us-east-1 --service ec2 --directory ./list_data/


Output::

  ---------------8<--(snippet)--8<---------------------
	
		--- ec2 us-east-1 DescribeVpcEndpoints None VpcEndpoints
		--- ec2 us-east-1 DescribeVpcPeeringConnections None VpcPeeringConnections
		--- ec2 us-east-1 DescribeVpcs None Vpcs
		--- ec2 us-east-1 DescribeVpnConnections None VpnConnections
		--- ec2 us-east-1 DescribeVpnGateways None VpnGateways
		--- ec2 us-east-1 ListImagesInRecycleBin None Images
		--- ec2 us-east-1 ListSnapshotsInRecycleBin None Snapshots
		+++ ec2 us-east-1 DescribeInstanceStatus None InstanceStatuses
		+++ ec2 us-east-1 DescribeInstances None Reservations
		+++ ec2 us-east-1 DescribeKeyPairs None KeyPairs
		+++ ec2 us-east-1 DescribeNetworkInterfaces None NetworkInterfaces
		+++ ec2 us-east-1 DescribeReplaceRootVolumeTasks None ReplaceRootVolumeTasks, truncated
		+++ ec2 us-east-1 DescribeSecurityGroupRules None SecurityGroupRules, truncated
		+++ ec2 us-east-1 DescribeSecurityGroups None SecurityGroups
		+++ ec2 us-east-1 DescribeTags None Tags
		+++ ec2 us-east-1 DescribeVolumeStatus None VolumeStatuses
		+++ ec2 us-east-1 DescribeVolumes None Volumes
		+++ ec2 us-east-1 GetVpnConnectionDeviceTypes None VpnConnectionDeviceTypes
		!!! ec2 us-east-1 DescribeInstanceEventNotificationAttributes None Exception('No listing: InstanceTagAttribute is no list:', {'InstanceTagAttribute': {'InstanceTagKeys': [], 'IncludeAllTagsOfInstance': False}})
		!!! ec2 us-east-1 DescribeTrunkInterfaceAssociations None ClientError('An error occurred (OperationNotPermitted) when calling the DescribeTrunkInterfaceAssociations operation: User 637333041330 is not permitted to perform this operation')
		!!! ec2 us-east-1 GetAssociatedEnclaveCertificateIamRoles None ClientError('An error occurred (InvalidCertificateArn.Malformed) when calling the GetAssociatedEnclaveCertificateIamRoles operation: The request must contain a valid certificate arn')
		!!! ec2 us-east-1 GetSerialConsoleAccessStatus None Exception('No listing: SerialConsoleAccessEnabled is no list:', {'SerialConsoleAccessEnabled': False})
		!!! ec2 us-east-1 GetTransitGatewayMulticastDomainAssociations None ClientError('An error occurred (MissingParameter) when calling the GetTransitGatewayMulticastDomainAssociations operation: Missing required parameter in request: TransitGatewayMulticastDomainId.') SamplingStatisticSummaries
--------------->8------------------>8---------------

- For queries with no limitation on  specific services enter:

beatdrift-cli $ aws-list-all query --region us-east-1 --directory ./listdata2/demo2


Truncated Output::

  ---------------8<--(snippet)--8<---------------------
	+++ appconfig us-east-1 ListDeploymentStrategies None Items
	+++ appstream us-east-1 DescribeImages None Images, truncated
	+++ athena us-east-1 ListDataCatalogs None DataCatalogsSummary
	+++ athena us-east-1 ListEngineVersions None EngineVersions
	+++ cloudfront None ListDistributions None Items, Distribution
	+++ cloudfront None ListOriginRequestPolicies None Items, OriginRequestPolicy
	+++ cloudfront None ListResponseHeadersPolicies None Items, ResponseHeadersPolicy
	+++ cloudwatch us-east-1 DescribeAlarms None CompositeAlarms, MetricAlarms
	+++ cloudwatch us-east-1 ListDashboards None DashboardEntries
	+++ cloudwatch us-east-1 ListMetrics None Metrics, truncated
	+++ docdb us-east-1 DescribeDBInstances None DBInstances
	+++ docdb us-east-1 DescribeDBSubnetGroups None DBSubnetGroups
	+++ docdb us-east-1 DescribePendingMaintenanceActions None PendingMaintenanceActions
	+++ dynamodb us-east-1 ListTables None TableNames
	+++ ec2 us-east-1 DescribeInstanceStatus None InstanceStatuses
	+++ ec2 us-east-1 DescribeInstances None Reservations
	+++ ec2 us-east-1 DescribeKeyPairs None KeyPairs
	+++ ec2 us-east-1 DescribeNetworkInterfaces None NetworkInterfaces
	+++ ec2 us-east-1 DescribeReplaceRootVolumeTasks None ReplaceRootVolumeTasks, truncated
	+++ ec2 us-east-1 DescribeSecurityGroupRules None SecurityGroupRules, truncated
	+++ ec2 us-east-1 DescribeSecurityGroups None SecurityGroups
	+++ ec2 us-east-1 DescribeTags None Tags
	+++ ec2 us-east-1 DescribeVolumeStatus None VolumeStatuses
	+++ ec2 us-east-1 DescribeVolumes None Volumes
	+++ ec2 us-east-1 GetVpnConnectionDeviceTypes None VpnConnectionDeviceTypes
	+++ ecs us-east-1 DescribeCapacityProviders None capacityProviders, failures
	+++ eks us-east-1 DescribeAddonVersions None addons
	+++ elasticache us-east-1 DescribeUsers None Users
	+++ emr us-east-1 ListReleaseLabels None ReleaseLabels, truncated
	+++ glue us-east-1 GetCrawlerMetrics None CrawlerMetricsList
	+++ glue us-east-1 GetCrawlers None Crawlers
	+++ glue us-east-1 GetDatabases None DatabaseList
	+++ glue us-east-1 GetResourcePolicies None GetResourcePoliciesResponseList, truncated
	+++ glue us-east-1 ListCrawlers None CrawlerNames
	+++ iam None ListAccessKeys None AccessKeyMetadata
	+++ iam None ListPolicies None Policies
	+++ iam None ListRoles None Roles
	+++ iam None ListSAMLProviders None SAMLProviderList
	+++ iam None ListUsers None Users
	+++ inspector us-east-1 ListFindings None findingArns, truncated
	
+++ rds us-east-1 DescribeDBSubnetGroups None DBSubnetGroups
+++ rds us-east-1 DescribePendingMaintenanceActions None PendingMaintenanceActions
+++ resource-groups us-east-1 ListGroups None GroupIdentifiers, Groups, truncated
+++ route53resolver us-east-1 ListFirewallConfigs None FirewallConfigs
+++ route53resolver us-east-1 ListFirewallDomainLists None FirewallDomainLists
+++ route53resolver us-east-1 ListResolverConfigs None ResolverConfigs
+++ s3 None ListBuckets None Buckets
+++ sagemaker us-east-1 ListModelMetadata None ModelMetadataSummaries
+++ schemas us-east-1 ListRegistries None Registries
+++ snowball us-east-1 ListCompatibleImages None CompatibleImages
+++ ssm us-east-1 ListCommandInvocations None CommandInvocations, truncated
>:| ce us-east-1 ListCostCategoryDefinitions None ClientError("An error occurred (AccessDeniedException) when calling the ListCostCategoryDefinitions operation: Failed to list Cost Categories: Linked account doesn't have access to cost category.")
>:| detective us-east-1 ListOrganizationAdminAccounts None ClientError('An error occurred (AccessDeniedException) when calling the ListOrganizationAdminAccounts operation: Caller is not an organization manager or delegated administrator')
>:| fms us-east-1 ListAppsLists None ClientError('An error occurred (AccessDeniedException) when calling the ListAppsLists operation: Account: 637333041330 is not currently delegated by AWS FM.')
>:| fms us-east-1 ListProtocolsLists None ClientError('An error occurred (AccessDeniedException) when calling the ListProtocolsLists operation: Account: 637333041330 is not currently delegated by AWS FM.')
--------------->8------------------>8---------------

In the list, the lines starting with:

 "``---``" means no resources of this type have been found, and
 if at least one resource of that sort has been found it displays  "``+++``".

"``>:|``" means that there is an error possibly due to missing permissions.

"``!!!``" appears at the beginning of the line in the list for other errors.

Currently, some default resources are still considered "user-created" and thus listed,
this may change in the future.

Details about found resources are saved in json files named after the service,
region, and operation used to find them. They can be dumped with::

  beatdrift-cli$ aws_list_all  show data/ec2_*
  beatdrift-cli$ aws_list_all show --verbose data/ec2_DescribeSecurityGroups_eu-west-1.json

Special treatment and removal of default resources which are performed by default during
data handling can be omitted with --unfilter and following arguments:
- cloudfront
- medialive
- ssmListCommands
- snsListSubscriptions
- athenaWorkGroups
- listEventBuses
- xRayGroups
- route53Resolver
- kmsListAliases
- appstreamImages
- cloudsearch
- cloudTrail
- cloudWatch
- iamPolicies
- s3Owner
- ecsClustersFailure
- pinpointGetApps
- ssmBaselines
- dbSecurityGroups
- dbParameterGroups
- dbClusterParameterGroups
- dbOptionGroups
- ec2VPC
- ec2Subnets
- ec2SecurityGroups
- ec2RouteTables
- ec2NetworkAcls
- ec2FpgaImages
- workmailDeletedOrganizations
- elasticacheSubnetGroups


How do I really list everything?
------------------------------------------------

Warning: As AWS has over 1024 API endpoints, you might have to increase the allowed number of open files on your end.
See https://github.com/Jase-The-Ace/beatdrift-cli/issues/

To open an issue and contribute to the project.

Restricting the region and. service is optional, a simple ``query`` without arguments lists everything.

A thread pool is used to run queries in parallel and randomize the order to avoid
hitting one endpoint in close succession. One run takes around three to 4 minutes on average based on your machine and connection.

More Examples
-------------

Add immediate, more verbose output to a query with ``--verbose``. Use twice for even more verbosity::

  beatdrift-cli$ aws_list_all query --region eu-west-1 --service ec2 --operation DescribeVpcs --directory data --verbose

Show resources for all returned queries::

  beatdrift-cli$ aws_list_all show --verbose data/*

Show resources for all ec2 returned queries::

  beatdrift-cli$ aws_list_all show --verbose data/ec2*

List available services to query::

  beatdrift-cli$ aws_list_all introspect list-services

List available operations for a given service, do::

  beatdrift-cli$ aws_list_all introspect list-operations --service ec2

List all resources in sequence to avoid throttling::

  beatdrift-cli$ aws_list_all query --parallel 1



- To create and use a virtual environment to isolate project from other versions of python on your machine:

- Install pip::

sudo easy_install pip

- Install virtualenv package

Enter this command into terminal::

sudo pip install virtualenv

or if you get an error enter this alternate command::

sudo -H pip install virtualenv

- Start virtualenv

Go to the place you want to store your code, then create a new directory::
mkdir test_project && cd test_project

While inside the 'test_project' folder/ directory, create a new virtualenv::

virtualenv env


source env/bin/activate


Github link: https://github.com/Jase-The-Ace/beatdrift-cli




