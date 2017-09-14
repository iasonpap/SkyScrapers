#include<stdio.h>
#include<stdlib.h>
#include<math.h>

double rndm (double max)
{
	double a=RAND_MAX/max;
	return rand()/a;
}

double gauss(double s)
{
	int i=0;
	double x,y,k;
	while(i<1)
	{
		x=2*rndm(1)-1;
		k=1/pow(2*s*s*3.14159265,1/2);
		y=rndm(k);
		if(y<=k*exp(-x*x/(s*s*s)))
		{
			i=3;
			
		}
	}
	return x;
}

double energy (double E,double DE)
{
	double e;
	e=E+DE*gauss(0.5);
	return e;
}



int main (void)
{
	int i,j,t,k=1;
	double A,Mion,M,Mtgt,N,d,Z1,Z2,DE,Earxiko,Q,ang,K,a,Energy,P,prop,x,xmax,b,sang,e,max,E[150],count[150],Emax;
	char fname;
	//eisagwgh dedomenwn kai statherwn//
	printf("Give Mion\n");
	scanf("%lf", &Mion);
	printf("\nGive Mtgt\n");
	scanf("%lf", &Mtgt);
	printf("\nGive the angle of the detector(deg)\n");
	scanf("%lf",&ang);
	M=Mtgt;
	ang=ang*0.0174532925;
	a=pow(1-(Mion/M)*(Mion/M)*sin(ang)*sin(ang),0.5);
	K=pow((a+(Mion/M)*cos(ang))/(1+(Mion/M)),2);
	printf("\n give the solid angle of the detector\n");
	scanf("%lf", &sang);
	printf("\n Give Z1\n");
	scanf("%lf", &Z1);
	printf("\n Give Z2\n");
	scanf("%lf", &Z2);
	printf("\n Give the energy(KeV)\n");
	scanf("%lf", &Earxiko);
	printf("\n Give the uncertainty(KeV)\n");
	scanf("%lf", &DE);
	printf("\n Give the  number of ions\n");
	scanf("%lf", &Q);
	printf("\n Give the density(grams/cm^3)\n");
	scanf("%lf", &N);
	printf("\n Give the atomic mass number\n");
	scanf("%lf", &A);
	printf("\n Give the energy loss (kev/cm)\n");
	scanf("%lf", &e);
	printf("\n Finaly give thickness (cm)\n");
	scanf("%lf", &d);
	
    while(k==1)
    {
	N=((6.02*(10e23))*N)/A;
	a=Z1*Z2*0.00144/10000;
	for(j=0;j<150;j++)
	{
		count[j]=0;
	}
	
	//basiko programma//
	for(i=0;i<Q;i++)
	{
		Energy=energy(Earxiko,DE);
		j=1;
		b=(a/(2*Energy))*cos(ang/2)/sin(ang/2);
		P=3.1415926536*b*b*sang*N*d;
		prop=rndm(1);
		if(prop<P)
		{
			xmax=((K)*Energy)/(K*e+e/cos(3.1415926536-ang));
			if(xmax>d)
			{
				Emax=(K)*Energy;
				//olla ok//
				max=(1/Emax)-(1/(Emax-d*(K*e+(e/cos(3.1415926536-ang)))));
				x=rndm(max);
				Energy=Emax/(1 -x*Emax);
			}
			else
			{
				Emax=(K)*Energy;
				//olla ok//
				max=(1/Emax)-(1/(Emax-xmax*(K*e+(e/cos(10*2.96704)))));
				x=rndm(max);
				Energy=Emax/(1 -x*Emax);
			}
		}
	if(prop<P)
		{
			for(j=0;j<150;j++)
			{
				if(Energy>50*e*(d/100)+K*Earxiko-(2*j+1)*(d/200)*(K*e+e/cos(3.1415926536-ang)))
				{
					count[j]=count[j]+1;
			        j=180;
				}
			}
		
		}
			
	}
	 
	FILE *fp;
	fp=fopen("energy-counts.txt","w");
	
	for(j=0;j<150;j++)
	{
		E[j]= 50*e*(d/100)+K*Earxiko-(2*j)*(d/200)*(K*e+e/cos(3.1415926536-ang));
	}
	
	for(j=0;j<150;j++)
		{
			fprintf(fp,"\n %lf	%lf" ,E[j],count[j]);
		}
	fclose(fp);
	
	printf("\nDo you want to run again for different energy,number of ions and \nthickness ?\n");
	printf("1.yes \n 2.no\n");
	scanf("%d", &k);
	if(k==1)
	{
		printf("\n Give the energy(KeV)\n");
	    scanf("%lf", &Earxiko);
	    printf("\n Give the uncertainty(KeV)\n");
	    scanf("%lf", &DE);
	    printf("\n Give the  number of ions\n");
	    scanf("%lf", &Q);
	    printf("\n Give the energy loss (kev/cm)\n");
	    scanf("%lf", &e);
	    printf("\n Finaly give thickness (cm)\n");
	    scanf("%lf", &d);
	}
    }
   return 0;
}
