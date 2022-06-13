# from terraformcore import *
from python_terraform import *

global tf
global approve
tf = Terraform(
        working_dir='/home/osboxes/terraform-stuff/')
tf.apply(skip_plan=True)
approve = {"auto-approve": True}
    
def init_terraform():
    print("\nInitializing Terraform directory....\n")
    return_code, stdout, stderr = tf.init(
            capture_output=True)
    print(stdout)
    print("\nInitializing completed....\n")

def terraform_format():
    print("\nPreparing for terraform format\n")
    return_code, stdout, stderr = tf.fmt(
            capture_output=True)
    print(stdout)
    print("\nFormatting completed....\n")

def terraform_validate():
    print("\nPreparing for terraform validate\n")
    return_code, stdout, stderr = tf.validate(
            capture_output=True)
    print(stdout)
    print("\nValidation completed....\n")

def terraform_plan():
        print("\nPreparing for terraform plan...\n")
        return_code, stdout, stderr = tf.plan(
            capture_output=True, out='plan.json')
        print(stdout)
        print("\nTerraform plan completed successfully\n")

def terraform_apply():
        print("\nPreparing for terraform apply....\n")
        return_code, stdout, stderr = tf.apply(
            capture_output=True, auto_approve=True, **approve)
        print(stdout)
        print("\nTerraform apply completed successfully\n")

def terraform_refresh():
        print("\nPreparing for terraform refresh....\n")
        return_code, stdout, stderr = tf.refresh(capture_output=True)
        print(stdout)
        print("\nTerraform refresh completed successfully\n")

while True:
    print("-----------Terraform AWS IaaC-----------\n")
    print("\n-------Select action to perform (1 - 7)-------\n")
    print("1 - To initialize Terraform directory")
    print("2 - To execute Terrfaform format (terraform fmt)")
    print("3 - To execute Terrfaform validate (terraform validate)")
    print("4 - To execute terraform plan. Before performing this action, make some changes to the provisioned resources in AWS console")
    print("5 - To execute Terrfaform apply")
    print("6 - To execute Terrfaform refresh")
    print("7 - To exit the CLI")

    terraform_action = int(input("\nEnter your choice: "))
    tf = Terraform(working_dir='/home/osboxes/terraform-stuff/')

    tf.apply(skip_plan=True)
    approve = {"auto-approve": True}

    if terraform_action == 1:
        init_terraform()
    elif terraform_action == 2:
        terraform_format()
    elif terraform_action == 3:
        terraform_validate()
    elif terraform_action == 4:
        terraform_plan()
    elif terraform_action == 5:
        terraform_apply()
    elif terraform_action == 6:
        terraform_refresh()
    elif terraform_action == 7:
        print("\nExiting Terraform CLI...\n")
        break
    else:
        print("\nEnter an option between 1 and 7\n")
