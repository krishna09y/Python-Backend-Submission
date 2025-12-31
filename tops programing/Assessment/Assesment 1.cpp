#include<stdio.h>
#include<string.h>
main()
{
	
	int code,quantity;
	
	char name[20];
	char moreorder[4]; 
	float totalBill = 0;
	
	
	printf("-FoodMenu-");
	printf("101. Burger - 60Rs ");
	printf("102. Pizza  - 120Rs ");
	printf("103. French Fries(180gm) - 90Rs ");
	printf("104. Cheese Spaghetti - 250Rs ");
	printf("105. Redsauce Pasta - 200Rs ");
	
	
	printf("----DrinksMenu----");
	printf("201. Cold Coffee - 80Rs ");
	printf("202. Mocha Coffee - 100Rs ");
	printf("203. Hazelnuts Coffee - 120Rs ");
	printf("204. Double Espresso - 110Rs ");
	printf("205. Dalgona Coffee - 150Rs ");
	
	do{
		printf("Enter the Item Code to Order :");
		scanf("%d",&code);
		
		printf("\nEnter quantity :");
		scanf("%d",&quantity);
		
		
		    
        if (code == 101) {
            totalBill += 60 * quantity;
            printf("Added %d x Burger = Rs. %d", quantity, 60 * quantity);
        } else if (code == 102) {
            totalBill += 120 * quantity;
            printf("Added %d x Pizza = Rs. %d", quantity, 120 * quantity);
        } else if (code == 103) {
            totalBill += 90 * quantity;
            printf("Added %d x French Fries = Rs. %d", quantity, 90 * quantity);
        } else if (code == 104) {
            totalBill += 250 * quantity;
            printf("Added %d x Cheese Spaghetti = Rs. %d", quantity, 250 * quantity);
        } else if (code == 105) {
            totalBill += 200 * quantity;
            printf("Added %d x Redsauce Pasta = Rs. %d", quantity, 200 * quantity);
        }

        else if (code == 201) {
            totalBill += 80 * quantity;
            printf("Added %d x Cold Coffee = Rs. %d\n", quantity, 80 * quantity);
        } else if (code == 202) {
            totalBill += 100 * quantity;
            printf("Added %d x Mocha Coffee = Rs. %d\n", quantity, 100 * quantity);
        } else if (code == 203) {
            totalBill += 120 * quantity;
            printf("Added %d x Hazelnuts Coffee = Rs. %d\n", quantity, 120 * quantity);
        } else if (code == 204) {
            totalBill += 110 * quantity;
            printf("Added %d x Double Espresso = Rs. %d\n", quantity, 110 * quantity);
        } else if (code == 205) {
            totalBill += 150 * quantity;
            printf("Added %d x Dalgona Coffee = Rs. %d\n", quantity, 150 * quantity);
        } else {
            printf("Invalid item code!");
        }
        
        
        printf("Do You Want To Order More? (yes/no) : ");
        	scanf("%s",moreorder);
        	
        	
	}while (strcmp(moreorder, "yes") == 0 || strcmp(moreorder, "YES") == 0);

  
    printf("== FINAL BILL ==");
    printf("Total amount: Rs. %.2f", totalBill);
    printf("Thank you for your order!");

}

