import argparse

# Setup argparse and create the arguments
# The epilog is for writing text at the bottom of your help menu, Just argparse.ArgumentParser() if you don't need it.
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, epilog='''
Examples:

Test Login: %(prog)s -t 10 -l ip_list.txt -u Bob -v
    ^Checks for successful login for Bob to each IP in ip_list.txt using 10 threads with verbose output.\n
!!Thanks for using this code!!
        ''', conflict_handler='resolve')

# Create some argument groups. These will separate the help section if need be. This can be ommitted if you don't
# wanna get fancy
group1 = parser.add_argument_group("Group 1", "Network Options")
group2 = parser.add_argument_group("Group 2", "General Options")
group3 = parser.add_argument_group("Group 3", "Added Features")

# Add group 1 options
# Standard argument that takes a string. It used the 2nd field as the name of the varible if dest is not set
group1.add_argument('-i', '--ip', help="Check a single target IP")
# choose the value of the variable in the args list. In this case we name it "iplist" using dest='name'
group1.add_argument('-l', '--list', dest='iplist', help="Check all targets in a list")
# Boolean option to use as a switch (store_true = True)
group1.add_argument('-f', '--force', action='store_true', help="Really do it no matter what!")

# Add group 2 options
group2.add_argument('-u', '--username', help="Username to use")
group2.add_argument('-U', '--user-list', dest='userlist', help="Username list")

# Add group 3 options
# Store an int with default values
group3.add_argument('-t', '--threads', default=5, type=int, help="Number of threads to use [default: 5]")
group3.add_argument('-v', '--verbose', action='store_true', help="Verbose output")


# Object that holds all arguments passed from command line
args = parser.parse_args()

# Bind each variable for easier reference and checking
ip = args.ip
iplist = args.iplist
threads = args.threads
verbose = args.verbose
username = args.username
userlist = args.userlist
force = args.force

if ip:
    print("Do stuff with ip if it was set")

if iplist:
    print("Do stuff with iplist if it was set")

if threads > 5:
    print("If threads is more than 5 do something")

if verbose:
    print("Do stuff with verbose if it was set")

if username:
    print("Do stuff with username if it was set")

if userlist:
    print("Do stuff with userlist if it was set")

if force:
    print("Do stuff with force if it was set")

