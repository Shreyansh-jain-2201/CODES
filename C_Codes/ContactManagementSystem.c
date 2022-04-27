// Develop a contact management system that allows the user to add, delete, and modify contacts.
// The program should do the following functions:

// [1] Add a new Contact
// [2] List all Contacts
// [3] Search for contact
// [4] Edit a Contact
// [5] Delete a Contact
// [0] Exit

// Create using a structure array

// The program should store data in files

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

struct Contacts
{
    char name[50];
    char phoneNumber[50];
    char email[50];
    char address[50];
};


void addContact(struct Contacts *contact[], int *size)
{
    int i;
    struct Contacts *newContact;
    newContact = (struct Contacts *)malloc(sizeof(struct Contacts));
    printf("Enter the name of the contact: ");
    scanf("%s", newContact->name);
    printf("Enter the phone number of the contact: ");
    scanf("%s", newContact->phoneNumber);
    printf("Enter the email of the contact: ");
    scanf("%s", newContact->email);
    printf("Enter the address of the contact: ");
    scanf("%s", newContact->address);
    contact[*size] = newContact;
    *size = *size + 1;
    return;
}

void listContacts(struct Contacts *contact[], int size)
{
    int i;
    for (i = 0; i < size; i++)
    {
        printf("Name: %s\n", contact[i]->name);
        printf("Phone Number: %s\n", contact[i]->phoneNumber);
        printf("Email: %s\n", contact[i]->email);
        printf("Address: %s\n", contact[i]->address);
    }
}

void searchContacts(struct Contacts *contact[], int size)
{
    int i;
    char searchName[50];
    printf("Enter the name of the contact you want to search: ");
    scanf("%s", searchName);
    for (i = 0; i < size; i++)
    {
        if (strcmp(contact[i]->name, searchName) == 0)
        {
            printf("Name: %s\n", contact[i]->name);
            printf("Phone Number: %s\n", contact[i]->phoneNumber);
            printf("Email: %s\n", contact[i]->email);
            printf("Address: %s\n", contact[i]->address);
        }
    }
}

void editContact(struct Contacts *contact[], int size)
{
    int i;
    char editName[50];
    printf("Enter the name of the contact you want to edit: ");
    scanf("%s", editName);
    for (i = 0; i < size; i++)
    {
        if (strcmp(contact[i]->name, editName) == 0)
        {
            printf("Enter the new name of the contact: ");
            scanf("%s", contact[i]->name);
            printf("Enter the new phone number of the contact: ");
            scanf("%s", contact[i]->phoneNumber);
            printf("Enter the new email of the contact: ");
            scanf("%s", contact[i]->email);
            printf("Enter the new address of the contact: ");
            scanf("%s", contact[i]->address);
        }
    }
}

void deleteContact(struct Contacts *contact[], int size)
{
    int i;
    char deleteName[50];
    printf("Enter the name of the contact you want to delete: ");
    scanf("%s", deleteName);
    for (i = 0; i < size; i++)
    {
        if (strcmp(contact[i]->name, deleteName) == 0)
        {
            contact[i] = contact[size - 1];
            contact[size - 1] = NULL;
            size = size - 1;
        }
    }

}

int askForChoice()
{
    int choice;
    printf("[1] Add a new Contact\n");
    printf("[2] List all Contacts\n");
    printf("[3] Search for contact\n");
    printf("[4] Edit a Contact\n");
    printf("[5] Delete a Contact\n");
    printf("[0] Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);
    return choice;
}

int main()
{
    int *size = 0;
    struct Contacts *contact[100];
    
    printf("Welcome to the contact management system!\n\n");
    // Ask for user choices in an infinite while loop
    // int choice;
    while(1)
    {
        int choice = askForChoice();
        // choice = askForChoice();
        switch (choice)
        {
            case 1:
                addContact(contact, size);
                // choice = askForChoice();
                
            case 2:
                listContacts(contact, *size);
                // choice = askForChoice();
            case 3:
                searchContacts(contact, *size);
                // choice = askForChoice();
            case 4:
                editContact(contact, *size);
                // choice =    askForChoice();
            case 5:
                deleteContact(contact, *size);
                choice = askForChoice();
            case 0:
                printf("Thank you for using the contact management system!\n");
                return 0;
            default:
                printf("Invalid choice!\n");
                // choice = askForChoice();
        }
    }
}