
print("\n")
import xlsxwriter

from os import system, name

# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def ec2():

    print("                                EC2 CF-Template Generator\n")


    saveFile = open ('EC2-instance-CF-Template.yaml','w')

    saveFile.write("""AWSTemplateFormatVersion: 2010-09-09
Parameters:
  VPCID:
    Type: 'List<AWS::EC2::VPC::Id>'
  SubnetOne:
    Type: 'List<AWS::EC2::Subnet::Id>'
  KeyPairs:
    Type: 'AWS::EC2::KeyPair::KeyName'
        
Resources:\n""")


    input("Press Enter to continue...")
    print("\n")

    clear()
    counter = 0

    while True:
    ##################################################################################


        InstanceCount = input("\nHow many instances of this size would you like?\n")
        InstanceAMIID = input("What is the AMI ID number?\n")

        #List the correct syntax options for the users#
        ans=True
        while ans:
            print ("""
            1. m4.large
            2. m4.xlarge
            3. m5.large
            4. m5.xlarge

            """)

         
            ans=input("Please Select allowable EC2 instance size) \n") 
            if ans=="1": 
              InstanceSize=("m4.large")
              break
            elif ans=="2":
              InstanceSize=("m4.xlarge")
              break
            elif ans=="3":
              InstanceSize=("m5.large")
              break
            elif ans=="4":
              InstanceSize=("m5.xlarge")
              break
            elif ans !="":
              print("\n Not Valid Choice Try again") 


        for i in range(0, int(InstanceCount)): 
            saveFile.write("  ec2cfinstance")
            saveFile.write(str(counter))
            saveFile.write(""":                       
    Type: AWS::EC2::Instance
    Properties:
      KeyName: !Ref KeyPairs""")
            saveFile.write("\n      ImageId: ")
            saveFile.write(InstanceAMIID)
            saveFile.write("\n")
            saveFile.write("      InstanceType: ")
            saveFile.write(InstanceSize)
            saveFile.write("\n")

            saveFile.write("""      Tags:
            - 
              Key: "Name"
              Value: "Group Deployment" \n\n""")
            counter = counter + 1


    ##################################################################################


        while True:
            answer = input("Run again? (y/n): ")
            if answer in ('y', 'n'):
                break
            print("\n Not Valid Choice Try again") 
        if answer == 'y':
            continue
        else:
            print("\n EC2-instance-CF-Template.yaml is your CloudFormation template.\n")
            saveFile.close()
            break

def vpc():

    print("\n")

    print("""                                VPC Creation

           ******Run this program in the same location desired for the output files******
           
         This Program will output the following 12 files:
         
         1. Program Input Values.txt: Record of values entered here by you
         2. 1AssignVPCCIDR.txt: CIDR block file to append to ticket subtask
         3. 2VPCYAMLTemplateGenerationSource.yaml: This will be used to generate the CloudFormation Template
         4. VPC ID.txt: Provide the VPC id from the AWS console and upload this file to the JIRA Ticket
         5. CSR.txt: Provide the CSR EC2 Instance id's and the Private ID Addresses
         6. Update Ticket.txt: Post execution user follow-up instructions
         7. VPC Complete.txt: To attach to the main ticket vault once VPC build is complete
         8. CSR Routing Diagram.txt: A breakdown diagram of the CRS Routing
         9. Splunk.txt: Fill out the Subnet information and attach it to the ticket
         10. Minion Renaming Tool.txt: Required for updating the minion renaming text on batch server
         11. PHZ.txt: Required to Associate PHZ
         12. VPC Peering.txt: Utilized to track VPC Peering information

         """)




    input("Press Enter to continue...")

    clear()

    print("\n Step 1: Assign a VPC CIDR Block\n")
    print("\n")


    TicketNum=input("What is the Ticket Number?(Reference JIRA Ticket):\n")
    print("\n")


    AWSAcc=input("What is the AWS Account Name?(Reference JIRA Ticket)\n")
    print("\n")


    VPCname = input("What is the VPC name?(Reference JIRA Ticket)\n")
    print("\n")


    clear()


    #List the correct syntax options for the users#
    ans=True
    while ans:
        print ("""
        1. small
        2. medium
        3. large
        4. extra large
        5. jumbo

        """)

     
        ans=input("Please Select a number that corresponds with the VPC size class(Reference JIRA Ticket) \n") 
        if ans=="1": 
          parent=("small")
          break
        elif ans=="2":
          parent=("medium")
          break
        elif ans=="3":
          parent=("large")
          break
        elif ans=="4":
          parent=("extra_large")
          break
        elif ans=="5":
          parent=("jumbo")
          break
        elif ans !="":
          print("\n Not Valid Choice Try again") 

    clear()



    print("\n")

    print("Account Name: ",AWSAcc)
    print("\n")

    print("VPC Name: ",VPCname)
    print("\n")
    dsh = input("What is the application name? (ex: bcda is the application name for a VPC Named: bcda-dev-vpc)\n")
    print("\n")

    mitg = input("Business Owner?(Reference JIRA Ticket)\n")
    print("\n")

    clear()

    ans=True
    while ans:
        print ("""
        1. prod
        2. test
        3. impl
        4. dev

        """)

     
        ans=input("Please Select a environment type(Reference JIRA Ticket) \n") 
        if ans=="1": 
          environment_name=("prod")
          break
        elif ans=="2":
          environment_name=("test")
          break
        elif ans=="3":
          environment_name=("impl")
          break
        elif ans=="4":
          environment_name=("dev")
          break
        elif ans !="":
          print("\n Not Valid Choice Try again") 

    clear()


    environment_type = environment_name



    bucket="cf-"+str.lower(dsh)+"-vpc-template/"+str(environment_name)


    clear()


    print("""Use http://jodies.de/ipcalc to verify CIDR Ranges

                                  Small /23 
                                 medium /22 
                                  large /21 
                                 Xlarge /20 
                                  Jumbo /19 """)

    print("\n")

    CIDR = input("What is the VPC CIDR? (x.x.x.x/x)\n")
    print("\n")
    IPADD=input("What is the VPC IP Address? (x.x.x.x) \n")


    saveFile = open ('Program Input Values.txt','w')
    saveFile.write("""Ticket Number: """+TicketNum+"""

Account Number: """+AWSAcc+"""

VPC Name: """+VPCname+"""

CIDR Class Size: """+parent+"""

Application Name: """+dsh+"""

Business Owner: """+mitg+"""

Environment Name: """+environment_name+"""

Environment Type: """+environment_type+"""

Bucket Name: """+bucket+"""

VPC CIDR: """+CIDR+"""

VPC IP Address: """+IPADD)

    saveFile.close()

          



    saveFile = open ('1AssignVPCCIDR.txt','w')
    saveFile.write("""AWS Account Name: """+AWSAcc+"""

VPC name: """+VPCname+"""

VPC CIDR: """+CIDR)
    saveFile.close()







    saveFile = open ('2VPCYAMLTemplateGenerationSource.yaml','w')

    saveFile.write("""parent: """+parent+"""
application_name: """+dsh+"""
business_name: """+mitg+"""
environment_name: """+environment_name+"""
environment_type: """+environment_type+"""
bucket_name: """+bucket+"""
vpc_address: """+IPADD+"""
hosted_zone_names: 
   - "{application_name}-{environment_name}.mp.cmscloud.local" """)
      
    saveFile.close()


    clear()




    print("*****************Upload reminder***************************************\n")

    # Workbook() takes one, non-optional, argument  
    # which is the filename that we want to create. 
    workbook =xlsxwriter.Workbook('Update Ticket.xlsx')
      
    bold   = workbook.add_format({'bold': True})
    cell_format1 = workbook.add_format({'bold': True})
    cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})

    worksheet = workbook.add_worksheet("Home Page")


    # Use the worksheet object to write 
    # data via the write() method.

    worksheet.write('B2', 'Ticket Number: ',cell_format1) 
    worksheet.write('D2', TicketNum)
    worksheet.write('B4', 'Account Name: ',cell_format1) 
    worksheet.write('D4', AWSAcc)
    worksheet.write('B6', 'VPC Name: ',cell_format1) 
    worksheet.write('D6', VPCname)
    worksheet.write('B6', 'VPC CIDR: ',cell_format1) 
    worksheet.write('D6', CIDR)
    worksheet.write('B8', 'Enter VPC ID  - ',cell_format1)
    worksheet.write('B9', 'VPC ID: ',cell_format1)




    # The workbook object is then used to add new  
    # worksheet via the add_worksheet() method. 
    worksheet = workbook.add_worksheet("SubTask1 - CIDR")

    # Use the worksheet object to write 
    # data via the write() method.


    worksheet.write('A1', 'Sub-Task 1: Assign VPC CIDR Block.',cell_format1)

    worksheet.write('B3', 'Determine an for the new VPC(from the spreadsheet or IPAM tool).',cell_format)

    worksheet.write('B5', 'Ticket Action Item: Upload "1AssignVPCCIDR" to the subtask of the ticket for reference.',cell_format)

    worksheet = workbook.add_worksheet("SubTask 2 - CF Template")



    # Finally, close the Excel file 
    # via the close() method. 
    workbook.close() 

    clear()

    print("Open 'Update Ticket.xlxs' and complete the remaining tasks")

    saveFile = open ('VPC ID.txt','w')
    saveFile.write("""

          VPC ID:

    """)
    saveFile.close()



    saveFile = open ('Splunk.txt','w')
    saveFile.write("""
                    Splunk 


AWS Account:"""+AWSAcc+"""

VPC Name:"""+VPCname+"""

VPC ID:

VPC IP: """+CIDR+"""

Subnets( i.e. 10.0.[1|2|3].*):


10..[|].*
       """)

    saveFile.close()



    saveFile = open ('PHZ.txt','w')
    saveFile.write("""
                    PHZ


AWS Account:"""+AWSAcc+"""

VPC Name:"""+VPCname+"""

VPC ID: 

Hosted Zone ID:

*if this is a new account, create a new profile on the config file*

Location: /home/<ID>/.aws/config

profile:

[profile <profile name>]
role_arn = arn:aws:iam::<account number>:role/enterprise-tools-role
credential_source = Ec2InstanceMetadata


Commands:
aws route53 create-vpc-association-authorization --hosted-zone-id <PHZ ID> --vpc VPCRegion=us-east-1,VPCId=vpc- --profile <profile name>
aws route53 associate-vpc-with-hosted-zone --hosted-zone-id <PHZ ID> --vpc VPCRegion=us-east-1,VPCId=vpc- --profile oc-dhcp


       """)

    saveFile.close()



    saveFile = open ('Minion Renaming Tool.txt','w')
    saveFile.write("""

                    Minion Renaming Tool Text


AWS Account:"""+AWSAcc+"""

VPC Name:"""+VPCname+"""

VPC CIDR: """+CIDR+""" 

 
Format: Account-Name-SubnetType-Region-RHEL,First-3-Octets.
*make sure you capture the entire VPC Subnet range*
ex.          CPM-123-IMPL-WEB-EAST-RHEL,2.3.4.
(Do this for WEB, APP, DAT,MGMT, DMZ, TRANS)

       """)

    saveFile.close()


    saveFile = open ('VPC Complete.txt','w')

    saveFile.write("""

VPC Name: """+VPCname+"""

VPC CIDR: """+CIDR+"""

VPC Id:

VPC Peering Information: """)

    saveFile.close()

    saveFile = open ('Nessus Onboarding.txt','w')

    saveFile.write("""

AWS Account Name: """+AWSAcc+"""
VPC name: """+VPCname+"""
Application Name: """+dsh+"""
Environment: """+environment_type+"""
VPC CIDR: """+CIDR+"""

 """)

    saveFile.close()

    saveFile = open ('VPC Peering.txt','w')

    saveFile.write("""

--------------------------
aws account 

Account ID 

VPC ID 

vpc name: """+VPCname+"""  

vpc CIDR: """+CIDR+""" 

Peering connection name
"""+VPCname+""" to 


     

    """)

    saveFile.close()


    input("Press Enter to continue...")


    import os
    os.system("start cmd")
      
################################################################################

def s3():
   saveFile = open ('S3 Bucket CF Template.yaml','w')
   saveFile.write("""

AWSTemplateFormatVersion: 2010-09-09
Parameters:
  BucketName:
    Default: 'please-change-bucket-name'
    Type: 'String'

Resources:
  internalalb:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Ref BucketName     # optional
      VersioningConfiguration:
        Status: Suspended
      Tags:                # optional, list of Tag
        -
          Key: "Name"
          Value: "S3 Bucket CF"
   """)
   saveFile.close()
   print("\n S3 Bucket CF Template.yaml is your CloudFormation template.\n")
   input("Press Enter to continue...")
   clear()

################################################################################
def rds_oracle_PROD():
   saveFile = open ('RDS Prod Oracle CF Template.yaml','w')
   saveFile.write("""

AWSTemplateFormatVersion: 2010-09-09

Parameters:
  Subnets:
    Type: 'List<AWS::EC2::Subnet::Id>'
  VPCID:
    Type: 'List<AWS::EC2::VPC::Id>'
  Username:
    Type: String
    Default: 'DatabaseAdmin'
  Password:
    Type: String
    Default: 'Password'
  NameofDataBase:
    Type: String
    Default: 'RDS PROD ORACLE'



Resources:
  rdsprodoracleenterprise:
    Type: 'AWS::RDS::DBInstance'
    Properties:
      AllocatedStorage: '100'
      AllowMajorVersionUpgrade: 'false'
      AutoMinorVersionUpgrade: 'true'
      CharacterSetName: AL32UTF8
      DBInstanceClass: db.r4.xlarge
      StorageType: io1
      BackupRetentionPeriod: '7'
      MasterUsername: !Ref Username
      MasterUserPassword: !Ref Password
      PreferredBackupWindow: '08:52-09:22'
      PreferredMaintenanceWindow: 'sat:07:33-sat:08:03'
      Iops: '1000'
      DBName: !Ref NameofDataBase
      Engine: oracle-ee
      EngineVersion: 12.1.0.2.v13
      LicenseModel: bring-your-own-license
      MultiAZ: 'true'

      Tags:
        - Key: workload-type
          Value: production
       
  dbsubnetdefault:
    Type: 'AWS::RDS::DBSubnetGroup'
    Properties:
      DBSubnetGroupDescription: default
      SubnetIds: !Ref Subnets
Description: RDS Oracle Database


   """)
   saveFile.close()
   print("\n RDS_Prod_Oracle_CF_Template.yaml is your CloudFormation template.\n")

   input("Press Enter to continue...")
   clear()

################################################################################
def source():
    saveFile = open ('Source.txt','w')

    saveFile.write("parent: ")
    saveFile.write("\n")
    saveFile.write("application_name: ")
    saveFile.write("\n")
    saveFile.write("business_name: ")
    saveFile.write("\n")
    saveFile.write("environment_name: ")
    saveFile.write("\n")
    saveFile.write("environment_type: ")
    saveFile.write("\n")
    saveFile.write("bucket_name: ")
    saveFile.write("\n")
    saveFile.write("vpc_address: ")
    saveFile.write("\n")
    saveFile.write("hosted_zone_names: ")
    saveFile.write("\n")
    saveFile.write("""   - "{application_name}-{environment_name}.mp.cmscloud.local"\n""")
      
    saveFile.close()
    print("\n Source.txt is your Stratiform Source format template.\n")
    input("Press Enter to continue...")
    clear()
################################################################################
def VPCBuild():

    ans=True
    while ans:
        print ("""
        1. VPC Records
        2. Stratiform Source Code Template


        """)

     
        ans=input("Please select one of the following options \n") 
        if ans=="1": 
          vpc()
          break
        elif ans=="2":
          source()
          break
        elif ans !="":
          print("\n Not Valid Choice Try again") 

    clear()
################################################################################
def database():
    ans=True
    while ans:
        print ("""
        1. RDS Oracle Prod
        2.         """)

     
        ans=input("\n Please Select a database type \n") 
        if ans=="1": 
          rds_oracle_PROD()
          break
        elif ans=="2":

          break
        elif ans !="":
          print("\n Not Valid Choice Try again") 

    clear()
    
################################################################################
def forms():
    ans=True
    while ans:
        print ("""
        1. RDS Request form
        2. EFS Request form
        3. ELB Request form
        4. Join to AD form
        5. VPC Peering form
        6. VPC Build Request form
        7. EC2 Request form\n""")

     
        ans=input("Please Select a form \n") 
        if ans=="1":
          clear()
          rdsform()
          break
        if ans=="2":
          clear()
          efsform()
          break
        if ans=="3":
          clear()
          elbform()
          break
        if ans=="4":
          clear()
          adjoinform()
          break
        if ans=="5":
          clear()
          vpcpeeringform()
          break
        if ans=="6":
          clear()
          vpcbuildform()
        if ans=="7":
          clear()
          ec2form()
          break
        elif ans !="":
          print("\n Not Valid Choice Try again") 

    clear()
################################################################################
def rdsform():
    print("""
DB Name:
DB Engine:
DB Size:
Encryption:
	Note: 1. Database Encryption will utilize Custom KMS Keys
              2. Prod Instance Must be Encrypted
Multi AZ:
	Note: Prod Instance Must be Multi-AZ
""")


    ans=True
    while ans:
        print ("""   ------------------------------------------------------

        1. No
        2. Yes""")

     
        ans=input("Output to text file\n") 
        if ans=="1": 
          break
        if ans=="2": 
          saveFile = open ('RDS Request.txt','w')

          saveFile.write("""
DB Name:
DB Engine:
DB Size:
Encryption:
	Note: 1. Database Encryption will utilize Custom KMS Keys
              2. Prod Instance Must be Encrypted
Multi AZ:
	Note: Prod Instance Must be Multi-AZ
""")

          saveFile.close()
          print("\n RDS Request.txt has been saved\n")
          break
        elif ans !="":
          print("\n Not Valid Choice Try again")

    input("Press Enter to continue...")
    clear()
################################################################################
def efsform():
    print("""
EFS Name:
VPC:
Subnet(s):
Mount to which Instance:
Encryption for data at rest:

""")


    ans=True
    while ans:
        print ("""   ------------------------------------------------------

        1. No
        2. Yes""")

     
        ans=input("Output to text file \n") 
        if ans=="1": 
          break
        if ans=="2": 
          saveFile = open ('EFS Request.txt','w')

          saveFile.write("""
EFS Name:
VPC:
Subnet(s):
Mount to which Instance:
Encryption for data at rest:

""")

          saveFile.close()
          print("\n EFS Request.txt has been saved\n")
          break
        elif ans !="":
          print("\n Not Valid Choice Try again")

    input("Press Enter to continue...")
    clear()
################################################################################
def elbform():
    print("""
Load Balancer:           (application or network)
LB Name: 
VPC Name:
	VPC Subnets:
Target Group Name:

""")


    ans=True
    while ans:
        print ("""   ------------------------------------------------------

        1. No
        2. Yes""")

     
        ans=input("Output to text file\n") 
        if ans=="1": 
          break
        if ans=="2": 
          saveFile = open ('ELB Request.txt','w')

          saveFile.write("""
Load Balancer:           (application or network)
LB Name: 
VPC Name:
	VPC Subnets:
Target Group Name:
""")

          saveFile.close()
          print("\n ELB Request.txt has been saved\n")
          break
        elif ans !="":
          print("\n Not Valid Choice Try again")

    input("Press Enter to continue...")
    clear()
################################################################################
def adjoinform():
    print("""
   Preferred Hostname(15 Character Limit):           Instance ID:               Instance IP:
1.
2.
3.

""")


    ans=True
    while ans:
        print ("""   ------------------------------------------------------

        1. No
        2. Yes""")

     
        ans=input("Output to text file \n") 
        if ans=="1": 
          break
        if ans=="2": 
          saveFile = open ('AD Join.txt','w')

          saveFile.write("""
   Preferred Hostname(15 Character Limit):           Instance ID:               Instance IP:
1.
2.
3.

""")

          saveFile.close()
          print("\n AD Join.txt has been saved\n")
          break
        elif ans !="":
          print("\n Not Valid Choice Try again")

    input("Press Enter to continue...")
    clear()
################################################################################
def vpcpeeringform():
    print("""
Source:

Account ID: 
Account Name: 
VPC ID: 
VPC Name: 
VPC CIDR(s): 
VPC Subnet(s): 
Requester Region: us-east-1


Destination:

Account ID: 
Account Name: 
VPC ID: 
VPC Name: 
VPC CIDR(s): 
VPC Subnet(s): 
Requester Region: us-east-1
""")


    ans=True
    while ans:
        print ("""   ------------------------------------------------------

        1. No
        2. Yes""")

     
        ans=input("Output to text file \n") 
        if ans=="1": 
          break
        if ans=="2": 
          saveFile = open ('VPC Peering.txt','w')

          saveFile.write("""
Source:

Account ID: 
Account Name: 
VPC ID: 
VPC Name: 
VPC CIDR(s): 
VPC Subnet(s): 
Requester Region: us-east-1


Destination:

Account ID: 
Account Name: 
VPC ID: 
VPC Name: 
VPC CIDR(s): 
VPC Subnet(s): 
Requester Region: us-east-1

""")

          saveFile.close()
          print("\n VPC Peering.txt has been saved\n")
          break
        elif ans !="":
          print("\n Not Valid Choice Try again")

    input("Press Enter to continue...")
    clear()
################################################################################
def vpcbuildform():
    print("""
AWS Account #: 
AWS Account Name: 
Business Owner: 
CIDR Size: 
VPC Name: 
(Dev/test/imp/prod/ss): 
Region: 
CSR throughput: 
Availability Zone Requirements (2 AZ or 1 AZ) : 



""")


    ans=True
    while ans:
        print ("""   ------------------------------------------------------

        1. No
        2. Yes""")

     
        ans=input("Output to Text \n") 
        if ans=="1": 
          break
        if ans=="2": 
          saveFile = open ('VPC Build.txt','w')

          saveFile.write("""
AWS Account #: 
AWS Account Name: 
Business Owner: 
CIDR Size: 
VPC Name: 
(Dev/test/imp/prod/ss): 
Region: 
CSR throughput: 
Availability Zone Requirements (2 AZ or 1 AZ) : 


Note:
* By default CCS Configures two CSRs per VPC, one in per availability zone (AZ1 & AZ2). In the event that the customer does not wish to have two availability zones, the CCS team will configure both of the CSRs in their respective AZs and shut down the secondary CSRs in AZ2.
* There is a sub-task for peering. If peering is required between this vpc and 
others within the account or in another account, please update the peering sub ticket to provide
details.
* By default CCS configures two 10Mbps CSRs for each VPC for a total throughput of 20 Mbps across three AZ's- 
If you believe that any environments will need more throughput, please specify
""")

          saveFile.close()
          print("\n VPC Build.txt has been saved\n")
          break
        elif ans !="":
          print("\n Not Valid Choice Try again")

    input("Press Enter to continue...")
    clear()
################################################################################
def ec2form():
    print("""
EC2 Name:
VPC:
Subnet:
EC2 OS:
Instance Size:
Encryption(EBS Volume):
Key:
Security Groups:
Termination Protection:
""")


    ans=True
    while ans:
        print ("""   ------------------------------------------------------

        1. No
        2. Yes""")

     
        ans=input("Output to text file \n") 
        if ans=="1": 
          break
        if ans=="2": 
          saveFile = open ('EC2 Request.txt','w')

          saveFile.write("""
EC2 Name:
VPC:
Subnet:
EC2 OS:
Instance Size:
Encryption(EBS Volume):
Key:
Security Groups:
Termination Protection:

""")

          saveFile.close()
          print("\n EC2 Request.txt has been saved\n")
          break
        elif ans !="":
          print("\n Not Valid Choice Try again")

    input("Press Enter to continue...")
    clear()
################################################################################

def file():
    print("\n                                EC2 File System Generator\n")






    input("Press Enter to continue...")
    print("\n")
    saveFile = open ('File-System.txt','w')
    saveFile.write("""

Copy and Paste the following text in terminal Window
_________________________________________________________________

pvcreate /dev/xvdb
vgcreate VolGroup01 /dev/xvdb   
    """)



    def CustomFileSystem():
        while True:

            clear()

            willmount=input("\n Please enter mount Point name: ")
            nextvol=input(" Please Enter Volume SubGroup: ")
            VolumeSize=input(" Please enter Volume Size: ")

            filetemplate ="""                                            
lvcreate -L {}G -n {} VolGroup01
mkfs.ext4 /dev/VolGroup01/{}           
mkdir /{}
mount /dev/VolGroup01/{} /{}




                  """.format(VolumeSize,nextvol,nextvol,willmount,nextvol,willmount)
            saveFile.write (filetemplate)
            clear()

            while True:
                answer = input("\nRun again? (y/n): ")
                if answer in ('y', 'n'):
                    break
                print("\n Not Valid Choice Try again") 
            if answer == 'y':
                continue
            else:
                print("""
_________________________________________________________________

Open File System.txt for your custom Template\n""")
                saveFile.write("""    *****Update /etc/fstab so that file systems are mountec at system boot.


                Example:
                        /dev/mapper/VolGroup01-Home              /Home              ext4   defaults,noatime,nofail 0 2""")
                saveFile.close()
                break




    def FileSystem():
        clear()
        saveFile.write ("""

Format and Paste the following text in terminal Window
_________________________________________________________________


pvcreate /dev/xvdb
vgcreate VolGroup01 /dev/xvdb                        
lvcreate -L 20G -n SecureSpan VolGroup01
mkfs.ext4 /dev/VolGroup01/SedcureSpan           
mkdir /opt/IBM
mount /dev/VolGroup01/SecureSpan /opt/IBM

_________________________________________________________________

    *****Update /etc/fstab so that file systems are mountec at system boot.

Example:
    /dev/mapper/VolGroup01-SecureSpan              /opt/IBM              ext4   defaults,noatime,nofail 0 2
    """)
        saveFile.close()
        print("""

Format and Paste the following text in terminal Window
_________________________________________________________________

pvcreate /dev/xvdb
vgcreate VolGroup01 /dev/xvdb                        
lvcreate -L 20G -n SecureSpan VolGroup01
mkfs.ext4 /dev/VolGroup01/SedcureSpan           
mkdir /opt/IBM
mount /dev/VolGroup01/SecureSpan /opt/IBM

_________________________________________________________________


    *****Update /etc/fstab so that file systems are mountec at system boot.

Example:
    /dev/mapper/VolGroup01-SecureSpan              /opt/IBM              ext4   defaults,noatime,nofail 0 2
    """)
        print("\n Open File-System.txt for the Template")
        input("Press Enter to continue...")


    #List the correct syntax options for the users#
    ans=True
    while ans:
        clear()
        print ("""
        1. Generate Custom File System Template
        2. EC2 File System Template  """)

     
        ans=input("\n Please Select from the following options: ") 
        if ans=="1": 
          CustomFileSystem()
          break
        elif ans=="2":
          FileSystem()
          break
        elif ans !="":
          print("\n Not Valid Choice Try again")

    input("Press Enter to continue...")

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################

################################################################################
def main():
    while True:
        

        #List the correct syntax options for the users#
        ans=True
        while ans:
            clear()
            print ("""
                                Terminal Services

            1. VPC
            2. (Coming Soon: Not a Valid Selection) CSR Configs
            3. (Munlti) EC2 CF Template Generator
            4. Database CF Template Generator (Requires Editing)
            5. Internal ALB CF Template Generator
            6. S3 Bucket CF Template Generator
            7. Target Group CF Template Generator
            8. Request Forms
            9. EC2 File System

            """)

         
            ans=input("\nPlease Choose a service\n")
            clear()

            if ans=="txt":
              saveFile = open ('Text File.txt','w')
              saveFile.close()
              break
            if ans=="1": 
              VPCBuild()
              break
            elif ans=="3":
              ec2()
              break
            elif ans=="4":
              database()
              break
            elif ans=="5":
              alb()
              break
            elif ans=="6":
              s3()
              break
            elif ans=="7":
              tg()
              break
            elif ans=="8":
              forms()
              break
            elif ans=="9":
              file()
              break
            elif ans !="":
              clear()
              print("\n Not Valid Choice Try again") 

        while True:
            answer = input("\n Select 'y' to return to Terminal Services or 'n' to Exit (y/n): ")
            if answer in ('y', 'n'):
                break
            print("\n Not Valid Choice Try again") 
        if answer == 'y':
            clear()
            continue
        else:
            print("\n Goodbye!\n")
            break


main()
