#include <iostream>
#include <math.h>
#include <ctime>
using namespace std;

bool isPrime(int num)
{
	if (num < 2)
		return false;

	for (int i = 2; i <= num - 1; i++)
		if (num % i == 0)
			return false;
	return true;
}

int findMaxPrime(int num)
{
	int max = 2;
	for (int i = 400000; i < num; i++)
		if (isPrime(i))
			if (i > max)
				max = i;
	return max;
}


void Task1()
{
	srand((unsigned)time(0));
	int i, randNum;

	do
	{
		i = (rand() % 100000) + 1;
	} while (!isPrime(i));
	cout << "The random prime less than 100000: " << i << endl;

	cout << "-------------------------------------------------" << endl << endl;

	cout << "The maximum prime less than 500000: " << findMaxPrime(500000) << endl;
	cout << "The maximum prime less than 1000000: " << findMaxPrime(1000000) << endl;


	cout << "Enter a random integer number: ";
	cin >> randNum;

	while (randNum >= 1000000 || randNum < 0)
	{
		cout << "Retype a random integer number: ";
		cin >> randNum;
	}

	if (isPrime(randNum))
		cout << randNum << " is a prime" << endl << endl;
	else
		cout << randNum << " isn't a prime" << endl << endl;

}
int gcd(int a, int b) 
{
	int tmp;
	while (b != 0) {
		tmp = a % b;
		a = b;
		b = tmp;
	}
	return a;
}
//a, b > 0, p phải là số nguyên tố
 int modPrimePow(long a, long b, int p)
{
	long ret = 1;
	a %= p;
	b %= p - 1;
	while (b > 0) //vòng lặp phân tích b thành cơ số 2
	{
		if (b % 2 > 0)  //ở vị trí có số 1 thì nhân với a^(2^i) tương ứng. Tất cả các phép nhân đều có phép mod p theo sau.
			ret = ret * a % p;
		a = a * a % p;  //tính tiếp a^(2^(i+1)), a^1 -> a^2 -> a^4 -> a^8 -> a^16 v.v...
		b /= 2;
	}
	return (int)ret;
}

void Task2()
{
	int a;
	int b;
	int c;
	cout << "Nhap a: \n"; cin >> a;
	cout << "Nhap b: \n"; cin >> b;
	c = gcd(a, b);
	cout << "Uoc chung lon nhat cua " << a << " va " << b << " la " << c << endl;
	cout << "-------------------------------------------------" << endl << endl;
}

void Task3()
{
	cout << "a^b mod p\n";
	long a;
	long b;
	int p;
	int kq;
	cout << "Nhap a: \n"; cin >> a;
	cout << "Nhap b: \n"; cin >> b;
	cout << "Nhap p: \n"; cin >> p;
	kq = modPrimePow(a, b, p);
	cout << a << " ^ " << b << " mod " << p << " = " << kq << endl;
}
void Menu()
{
	cout << "-------------------------------Menu-------------------------------" << endl;
	cout << " 1.Phat sinh so nguyen to\n";
	cout << " 2.Kiem tra Uoc chung lon nhat\n";
	cout << " 3.Tinh a^b mod p\n";
	cout << " 0.Thoat \n";
}




int main()
{
	while (true)
	{
		Menu();
		int luachon;
		cout << "Nhap lua chon: \n";
		cin >> luachon;

		switch (luachon)
		{
		case 1:
			Task1();
			break;
		case 2:
			Task2();
			break;
		case 3:
			Task3();
			break;
		case 0:
			exit(1);
			break;
		default:
			exit(1);
			break;
		}
	}
	system("pause");
	return 0;
}
