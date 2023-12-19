from dao.InsuranceServiceImpl import InsuranceServiceImpl
from dao.UserDAO import UserDAO
from dao.PolicyDAO import PolicyDAO
from dao.ClientDAO import ClientDAO
from dao.ClaimDAO import ClaimDAO
from dao.PaymentDAO import PaymentDAO
from exception.PolicyNotFoundException import PolicyNotFoundException
from util.DBConnUtil import DBConnection


def main():

    dbconnection = DBConnection()

    try:
        dbconnection.open()
        print("--Database Is Connected:--")
    except Exception as e:
        print(e)

    try:
        print("=" * 30)
        print("Insurance Management System")
        print("=" * 30)
        print("Welcome to Insurance Management System!")

        insurance_management_system = InsuranceServiceImpl()

        while True:
            print("1.User 2.Policy 3.Client 4.Claim 5.Payment 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                u = UserDAO()
                u.perform_user_actions()
            elif ch == 2:
                p = PolicyDAO()
                p.perform_policy_actions()
            elif ch == 3:
                c = ClientDAO()
                c.perform_client_actions()
            elif ch == 4:
                cl = ClaimDAO()
                cl.perform_claim_actions()
            elif ch == 5:
                pp = PaymentDAO()
                pp.perform_payment_actions()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

        while True:
            print("=" * 10)
            print("---MENU---")
            print("=" * 10)
            print("1.getPolicy\n2.getAllPolicies\n0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                print(insurance_management_system.getPolicy(int(input('Enter Policy ID to get details: '))))
            elif ch == 2:
                print(f'List of all Policies: {insurance_management_system.getAllPolicies()}')
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    except PolicyNotFoundException as e:
        print(e)

    except Exception as e:
        print(e)

    finally:
        dbconnection.close()
        print("Thankyou for visiting Insurance Management System!")
        print("--Connection Is Closed:--")


if __name__ == "__main__":
    main()
