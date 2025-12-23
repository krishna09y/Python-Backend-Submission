#include<stdio.h>
#include<string.h>
main()
{
	
	int code,quantity;
	
	char name[20];
	char moreorder[4]; // for yes/no input
	float totalBill = 0;
	
	// Display Food Menu Once
	printf("------FoodMenu------\n");
	printf("101. Burger - 60Rs \n");
	printf("102. Pizza  - 120Rs \n");
	printf("103. French Fries(180gm) - 90Rs \n");
	printf("104. Cheese Spaghetti - 250Rs \n");
	printf("105. Redsauce Pasta - 200Rs \n");
	
	// Display Drinks Menu Once
	printf("----DrinksMenu----\n");
	printf("201. Cold Coffee - 80Rs \n");
	printf("202. Mocha Coffee - 100Rs \n");
	printf("203. Hazelnuts Coffee - 120Rs \n");
	printf("204. Double Espresso - 110Rs \n");
	printf("205. Dalgona Coffee - 150Rs \n");
	
	do{
		printf("\nEnter the Item Code to Order :");
		scanf("%d",&code);
		
		printf("\nEnter quantity :");
		scanf("%d",&quantity);
		
		
		    // Food Items
        if (code == 101) {
            totalBill += 60 * quantity;
            printf("Added %d x Burger = Rs. %d\n", quantity, 60 * quantity);
        } else if (code == 102) {
            totalBill += 120 * quantity;
            printf("Added %d x Pizza = Rs. %d\n", quantity, 120 * quantity);
        } else if (code == 103) {
            totalBill += 90 * quantity;
            printf("Added %d x French Fries = Rs. %d\n", quantity, 90 * quantity);
        } else if (code == 104) {
            totalBill += 250 * quantity;
            printf("Added %d x Cheese Spaghetti = Rs. %d\n", quantity, 250 * quantity);
        } else if (code == 105) {
            totalBill += 200 * quantity;
            printf("Added %d x Redsauce Pasta = Rs. %d\n", quantity, 200 * quantity);
        }

        // Drink Items
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
            printf("Invalid item code!\n");
        }
        
        //Ask for more order 
        printf("Do You Want To Order More? (yes/no) : ");
        	scanf("%s",moreorder);
        	
        	
	}while (strcmp(moreorder, "yes") == 0 || strcmp(moreorder, "YES") == 0);

    // Final bill
    printf("\n========== FINAL BILL ==========\n");
    printf("Total amount: Rs. %.2f\n", totalBill);
    printf("Thank you for your order!\n");

}
