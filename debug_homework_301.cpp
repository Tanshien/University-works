#include<stdio.h>
int s_1 = 0,s_2 = 0;
int isTrue(int num_1,int num_2){
	int a[num_1]={0},b[num_2]={0},sum_1 = 0,sum_2 = 0;
	
	for(int i = 1;i < num_1;i++){
		if(num_1 % i == 0){
			a[s_1] = i;
			s_1++;
		}
	}
	
	for(int j = 1;j < num_2;j++){
		if(num_2 % j ==0){
			b[s_2] = j;
			s_2++;
		}
	}
	
	for(int i = 0;i <num_1;i++)
		sum_1 += a[i];
	
	for(int j = 0;j < num_2;j++)
		sum_2 += b[j];
	
	if(sum_1 == num_2 && sum_2 == num_1)
		return 1;
	
	else
		return 0;
}

int main()
{
	int n,m;
	scanf("%d %d",&n,&m);
	
	if(isTrue(n,m) == 1)
		printf("yes %d %d",s_1,s_2);
	
	else
		printf("no %d %d",s_1,s_2);
	
	
	return 0;
}
