namespace _26_2024
{
    internal class Program
{
    static void Main(string[] args)
    {
        StreamReader reader = new StreamReader("C:\\Users\\Manul\\Downloads\\26_17537.txt");
        string[] nmk = reader.ReadLine().Split(' ');
        int n = int.Parse(nmk[0]); // кол-во занятых мест
        int m = int.Parse(nmk[1]); // кол-во рядов в зале
        int k = int.Parse(nmk[2]); // кол-во мест в каждом ряду
        int[,] AllSeats = new int[m, k];
        int CurRow = new int();
        int CurSeat = new int();

        // Создаём двумерный массив со всеми занятыми местами
        for (int i = 0; i < n; i++)
        {
            string[] CurrentSeat = reader.ReadLine().Split(' ');
            CurRow = int.Parse(CurrentSeat[0]);
            CurSeat = int.Parse(CurrentSeat[1]);
            AllSeats[CurRow - 1, CurSeat - 1] = 1;
        }

        //Находим количество пустых мест перед каждым из занятых (я хз, как это объяснить)
        int[] FreeSeats = new int[k];
        for (int seat = 0; seat < k; seat++)
        {
            int counter = 0;
            for (int row = 0; row < m; row++)
            {
                if (AllSeats[row, seat] == 1)
                {
                    FreeSeats[seat] = counter;
                    break;
                }
                else
                {
                    counter++;
                }
                if (counter == m)
                {
                    FreeSeats[seat] = m;
                }
            }
        }

        //Находим два пустых места подходящих под условие
        int MaxRow = -1;
        int SeatNum = -1;
        for (int j = 0; j < (k - 1); j++)
        {
            if ((FreeSeats[j] <= FreeSeats[j + 1]) && FreeSeats[j] > MaxRow)
            {
                MaxRow = FreeSeats[j];
                SeatNum = (j + 1) + 1; // к номеру второго места прибавляем ещё 1, т.к. нумерация по условию идёт с 1
            }
        }
        Console.WriteLine(MaxRow + " " + SeatNum);
    }
}
}
