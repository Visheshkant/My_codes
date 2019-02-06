import java.util.*;
class Switch1
{
	public static void main(String []Vishesh_bank)
	{
		Scanner kb=new Scanner(System.in);
		System.out.println("\n");
		System.out.println("          _________Hello___________        ");
		System.out.println("\n");
		System.out.println("__________Welcome To Vishesh_Bank____________");
		System.out.println("\n");
		int balance,withdraw,choise,amount,note,i;
		balance=20000;
		System.out.println("Press 1: BALANCE ENQUERY");
		System.out.println("\n");
		System.out.println("Press 2: CASH WITHDRAWAL");
		System.out.println("\n");
		System.out.println("Press 3: CASH DEPOSIT");
		System.out.println("\n");
		System.out.println("Press 4: CHANGE PIN");
		System.out.println("\n");
		System.out.println("Press 5: MINI STATEMENT");
		System.out.println("\n");
		System.out.println("Press 6: MONEY TRANSFER");
		System.out.println("\n");
		choise=kb.nextInt();
		switch(choise)
		{
			case 1:System.out.println("_________Hello___________");
			System.out.println("\n");
            System.out.println("Please enter your pin.");
            String S_pin=new String();
            S_pin=kb.next();
			System.out.println("Your Current Balance Is:" +balance);
			break;

			case 2:System.out.println("_________Hello___________");
			System.out.println("\n");
			System.out.println("Enter the amount to be withdrawn?");
			withdraw=kb.nextInt();
			if(withdraw>balance)
			{
				System.out.println("____You don't have enough balance____");
			}
            else
            {
                System.out.println("\n");
                System.out.println("Enter the denominations you want to start from.");
                System.out.printf("2000");
                System.out.printf("\t");
                System.out.printf("1000");
                System.out.printf("\t");
                System.out.printf("500");
                System.out.printf("\t");
                System.out.printf("100");
                System.out.printf("\t");
                System.out.printf("50");
                System.out.printf("\t");
                System.out.printf("20");
                System.out.printf("\t");
                System.out.printf("10");
                System.out.printf("\t");
                System.out.printf("1");
                System.out.printf("\n");
                choise=kb.nextInt();
                switch(choise)
                {
            	     case 2000: note=withdraw/2000;
            	     System.out.println("Total Rs_2000 note: " +note);
            	     withdraw=withdraw%2000;

            	     case 1000: note=withdraw/1000;
            	     System.out.println("Total Rs_1000 note: " +note);
            	     withdraw=withdraw%1000;  
                      
                     case 500: note=withdraw/500;
            	     System.out.println("Total Rs_500 note: " +note);
            	     withdraw=withdraw%500;   
                     
                     case 100: note=withdraw/100;
            	     System.out.println("Total Rs_100 note: " +note);
            	     withdraw=withdraw%100;

            	     case 50: note=withdraw/50;
            	     System.out.println("Total Rs_50 note: " +note);
            	     withdraw=withdraw%50;

            	     case 20: note=withdraw/20;
            	     System.out.println("Total Rs_20 note: " +note);
            	     withdraw=withdraw%20;  

            	     case 10: note=withdraw/10;
            	     System.out.println("Total Rs_10 note: " +note);
            	     withdraw=withdraw%10;  

            	     case 1: note=withdraw/1;
            	     System.out.println("Total Rs_1 note: " +note);
            	     withdraw=withdraw%1; 
            	     break; 

            	     default:
            	     System.out.println("____Entered denominations are incorrect___");  
                }
            }
            break;
            case 3:System.out.printf("\n");
            System.out.println("_____Enter the amount to be deposited___");
            int new_amount=kb.nextInt();
            amount=balance+new_amount;
            System.out.println("Your amount after deposition is:" +amount);
            break;

            case 4:System.out.println("_____Enter your new 4-digit pin___");
            int n=0,count=2;
                String s1=new String ();
            	s1=kb.next();
                while(s1.length()!=4)
                {
                    System.out.println("Pin code shall be of 4 characters.You might want to enter it again!!!!");
                    System.out.println("You have "+count+" chance left");
                    --count;
                    s1=kb.next();
                    ++n;
                    if(n==2)
                    {
                        System.out.println("Sorry,you have to try after 48 hour!!!");
                        break;
                    }
                }
                if(s1.length()==4)
                {
                    System.out.println("____Enter to confirm____");
                    String s2=new String ();
                    int t=0;
            	    s2=kb.next();
                    boolean Equal=s1.equals(s2); 
                    if(Equal==false)
                    {
                        while(Equal==false)
                        {
            	           System.out.println("OOPS!!! It seems your passwprd does not match");
                           System.out.println("Please re-enter your password");
                           s2=kb.next();
                           Equal=s1.equals(s2);
            	           ++t;
                           if(t==2)
                           {
                              System.out.println("Sorry try it after 48 hour!!!");
                              break;
                           }
                        }
                    }
                    if(Equal==true)
                    {
                        System.out.println("Your new generated pin is");
                        System.out.println("---->>" +s2);
                    }  
                }
                break;
            case 5:
            System.out.println(" ________SORRY!!!________");
            System.out.println("\n");
            System.out.println("___We can't provide you with receipt___");
            break;

            case 6:
            System.out.println("Enter the receipients account number.");
            int num=kb.nextInt();
            System.out.println("Enter the amount to be transfered.");
            int money=kb.nextInt();
            System.out.println("Rs "+money + " is transfered");
            amount=balance-money;
            System.out.println("Now your current balance is:" +amount);
            break;

            default:
            System.out.println("**Invalid choice**");

		}
            
	}
}