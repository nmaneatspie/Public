/*	Program by Norman TXXXX, Last Updated 23/04/2020

	Program made to complete mission 1 of programming tasks on HackThisSite.com
	This program will store the words in a txt file in an array and then attempt
	accept jumbled inputs that match the words in the file. It will then locate
	the correct unjumbled word.
	
	This program is rather slow as it uses linear searches but attempts are made
	to reduce the group size of words to look at.
	
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define numwords 1275
#define BUF 10
#define filename "wordlist.txt"

int main(int argc, char **argv)
{
	char *input = argv[1];
	if(argc != 2 || input == NULL)
	{
		perror("Invalid (number of) inputs");
		return(-1);
	}
	
	if(strlen(input) > BUF)
	{
		perror("Input too large");
		return(-1);
	}

	char *findJumbledWord(char * jumbled, char wordlist[numwords][BUF]);
	
	FILE *file = fopen(filename, "r");
	char words[numwords][BUF];
	int filesize = 0;
	short i = 0;
	short counter = 0;
	
	if(file == NULL) {
	      perror("Error opening file");
	      return(-1);
	}
	
	//determine file size
	fseek(file, 0L, SEEK_END);
	filesize = ftell(file);
	fseek(file, 0L, SEEK_SET);
	
	// move file contents into a large string
	char *charArr = malloc(++filesize * sizeof(*charArr));
	char charIn;
	i = -1;
	
	do{
		if(feof(file))
		{
			break;
		}
		
		charIn = fgetc(file);
		++i;
			
		charArr[i] = charIn;

	} while(charIn && i < filesize-4);
	charArr[strlen(charArr)] = '\0';
	
	fclose(file);
		
	
        const char delim[2] = "\n";
	
	//split string content into words in array
	if(charArr != NULL){ 
		i = 0;
		char *token = strtok(charArr, delim);
		strcpy(words[i], token);
		for(i = 1; token != NULL && i < numwords; ++i)
		{

			token = strtok(NULL, delim);
			
			for(int j = 0; j < strlen(token); ++j)
			{
				if(token[j] == '\n' || token[j] == '\r')
				{
					token[j] = '\0';
				}
			}
			
			strcpy(words[i], token);

		}
	}
	
	free(charArr); 	

	file = fopen("answer.txt", "a");
	
	char *answer = findJumbledWord(input, words);
	
	fprintf(file, "%s,", answer);
	printf("%s\n", answer);
	
	free(answer);
		
	fclose(file);


   return(0);
}

//assumes the word exists in list provided and word is unique
char *findJumbledWord(char *jumbled, char wordlist[numwords][BUF]) 
{	
	short i,j = 0;
	short countermem = 0; //track num of words in templist
	char *templist[numwords];
	
	//mem allocation
	for(i = 0; i < numwords; ++i)
	{
		templist[i] = malloc(BUF * sizeof(*templist[i]));
	}

	//find equal length strings
	for(i = 0; i < numwords; ++i)
	{
		if(strlen(jumbled) == strlen(wordlist[i]))
		{
			strcpy(templist[countermem], wordlist[i]);
			++countermem;
		}
	}

	//free unused memory
	for(i = countermem; i < numwords; ++i)
	{
		if(templist[i] != NULL){
			free(templist[i]);
		}
	}

	//reduce list size to contents that hold first character in word
	short k = 0;
	short temp = countermem;
	
	while(temp > 1 && k < strlen(jumbled))
	{		
		char toFind = jumbled[k];
		countermem = 0;
		
		//find char in wordlist
		for(i = 0; i < temp; ++i)
		{
			char found = 'f';
			for(j = 0; j < BUF || templist[i][j] != '\0'; j++)
			{
				if(templist[i][j] == '\0')
				{
					break;
				} else if(templist[i][j] == toFind)
				{
					strcpy(templist[countermem], templist[i]);
					++countermem;
					found = 't';
					break;
				}
			}
			if(found == 'f'){
				strcpy(templist[i], "0");
			}
		}
		
		//free unused memory
		for(i = countermem; i < temp; ++i)
		{
			if(templist[i] == "0"){
				free(templist[i]);
			}
		}
		
		if(k < BUF)
		{
			k++;
		} else{break;}
		
		temp = countermem;
	}
	
	if(countermem < 0)
	{
		return("ERROR Countermem < 0");
	}

	//to reduce list if needed...this occurs normally when there is double or more of a char
	char enabled = 't';
 	if(countermem > 0 && enabled == 't'){
	
		char *moreChar = malloc(BUF * sizeof(*moreChar)); //hold the chars that exist multiple times
		short *count = malloc(BUF * sizeof(*count)); //hold the count for each multiple char
		short counter = 0;
		
		for(i = 0; i < BUF && jumbled[i] != '\0'; ++i)
		{
			for(j = i; j < BUF && jumbled[j] != '\0'; ++j)
			{
				if(jumbled[j] == '\0')
				{
					break;
				}
				
				if(jumbled[i] == jumbled[j])
				{
					moreChar[counter] = jumbled[i];
					++count[counter];
				}
			}
			++counter;
		}

		//reduce array size
		moreChar = realloc(moreChar, counter * sizeof(*moreChar));
		count = realloc(count, counter * sizeof(*count));
		
		//make list unique
		char *tempChar = malloc(counter * sizeof(*tempChar));
		short *tempCount = malloc(counter * sizeof(*tempCount));
		short tempCounter = 0;
		
		for(i = 0; i < counter; ++i)//larger count from left side
		{
			if(moreChar[i] == '\0') //null if found non-unique char
			{
				continue;
			}
			
			for(j = i+1; j < counter; ++j)
			{
				if(moreChar[j] == '\0')
				{
					continue;
				}

				if(moreChar[i] == moreChar[j])
				{
					moreChar[j] == '\0';					
					break;
				}
			}
			tempChar[tempCounter] = moreChar[i];
			tempCount[tempCounter] = count[i];
			++tempCounter;
		}
		--tempCounter; //remove the extra count
		
		free(moreChar);
		free(count);
		
		moreChar = tempChar;
		
		count = tempCount;
		counter = tempCounter; 
		
		//compare number of each chars in each remaining word to expected number of each char in jumbled word
		tempCount = malloc(counter * sizeof(*tempCount));
		
	 	for(i = 0; i < countermem; ++i) //loop for words
		{
			
			for(j = 0; j < counter; ++j)
			{
				tempCount[j] = count[j];
			}

			
			for(j = 0; j < BUF && templist[i][j] != '\0'; ++j) //loop for each char in word
			{
				for(k = 0; k < counter; ++k) //loop for each char in moreChar
				{
					if(templist[i][j] == moreChar[k])
					{
						--tempCount[k];
					}
				}
			}
			
			char same = 't';
			for(j = 0; j < counter; ++j)
			{
				if(tempCount[j] != 0)
				{
					same = 'f';
					break;
				}
			}
			
			if(same == 't')
			{
				strcpy(templist[0], templist[i]);
				break;
			}
			

		}
		
		free(tempCount);
		free(moreChar);
		free(count);
	}

	//temp
	char *foundWord = malloc(strlen(templist[0]) * sizeof(*foundWord));
	
	if(templist[0] != NULL)
	{
		strcpy(foundWord, templist[0]);
	}
	
	//free heap memory allocation
 	for(i = 0; i < countermem; ++i)
	{
		if(templist[i] != NULL)
		{
			free(templist[i]);
		}
	}

	if(foundWord != NULL)
	{
		return(foundWord);
	}
	
	return("ERROR");
}
