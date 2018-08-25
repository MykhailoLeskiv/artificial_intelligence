using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Media;
using System.Windows.Forms;

namespace Lab_3_Cs
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }
    }

    class ChoiceTree
    {
        public static int count = 0;
        public ChoiceTree()
        { }
        public static int[,] A = new int[3, 3] { { -5, -5, -5 }, { -5, -5, -5 }, { -5, -5, -5 } };
        public static bool EnemyAttack()
        {
            for (int i = 0; i < 3; i++)
                if (A[i, 0] + A[i, 1] + A[i, 2] == -3)
                {
                    for (int j = 0; j < 3; j++)
                    {
                        if (A[i, j] == -5)
                        {
                            A[i, j] = 0;
                            Form1.SetButton(i, j, "O");
                            break;
                        }
                    }
                    return true;
                }
            if (A[0, 0] + A[1, 1] + A[2, 2] == -3)
            {
                if (A[0, 0] == -5)
                {
                    A[0, 0] = 0;
                    Form1.SetButton(0, 0, "O");
                }
                else if (A[1, 1] == -5)
                {
                    A[1, 1] = 0;
                    Form1.SetButton(1, 1, "O");
                }
                else
                {
                    A[2, 2] = 0;
                    Form1.SetButton(2, 2, "O");
                }
                return true;
            }
            if (A[0, 2] + A[1, 1] + A[2, 0] == -3)
            {
                if (A[0, 2] == -5)
                {
                    A[0, 2] = 0;
                    Form1.SetButton(0, 2, "O");
                }
                else if (A[1, 1] == -5)
                {
                    A[1, 1] = 0;
                    Form1.SetButton(1, 1, "O");
                }
                else
                {
                    A[2, 0] = 0;
                    Form1.SetButton(2, 0, "O");
                }
                return true;
            }
            for (int i = 0; i < 3; i++)
                if (A[0, i] + A[1, i] + A[2, i] == -3)
                {
                    for (int j = 0; j < 3; j++)
                    {
                        if (A[j, i] == -5)
                        {
                            A[j, i] = 0;
                            Form1.SetButton(j, i, "O");
                            break;
                        }
                    }
                    return true;
                }
            return false;
        }
        public static bool PlayerError()
        {
            for (int i = 0; i < 3; i++)
                if (A[i, 0] + A[i, 1] + A[i, 2] == -5)
                {
                    for (int j = 0; j < 3; j++)
                    {
                        if (A[i, j] == -5)
                        {
                            A[i, j] = 0;
                            Form1.SetButton(i, j, "O");
                            break;
                        }
                    }
                    return true;
                }
            if (A[0, 0] + A[1, 1] + A[2, 2] == -5)
            {
                if (A[0, 0] == -5)
                {
                    A[0, 0] = 0;
                    Form1.SetButton(0, 0, "O");
                }
                else if (A[1, 1] == -5)
                {
                    A[1, 1] = 0;
                    Form1.SetButton(1, 1, "O");
                }
                else
                {
                    A[2, 2] = 0;
                    Form1.SetButton(2, 2, "O");
                }
                return true;
            }
            if (A[0, 2] + A[1, 1] + A[2, 0] == -5)
            {
                if (A[0, 2] == -5)
                {
                    A[0, 2] = 0;
                    Form1.SetButton(0, 2, "O");
                }
                else if (A[1, 1] == -5)
                {
                    A[1, 1] = 0;
                    Form1.SetButton(1, 1, "O");
                }
                else
                {
                    A[2, 0] = 0;
                    Form1.SetButton(2, 0, "O");
                }
                return true;
            }
            for (int i = 0; i < 3; i++)
                if (A[0, i] + A[1, i] + A[2, i] == -5)
                {
                    for (int j = 0; j < 3; j++)
                    {
                        if (A[j, i] == -5)
                        {
                            A[j, i] = 0;
                            Form1.SetButton(j, i, "O");
                            break;
                        }
                    }
                    return true;
                }
            return false;
        }
        public static bool Winning()
        {
            for (int i = 0; i < 3; i++)
                if (A[i, 0] + A[i, 1] + A[i, 2] == 0)
                {
                    Form1.SetColor(i, 0, true);
                    Form1.SetColor(i, 1, true);
                    Form1.SetColor(i, 2, true);
                    return true;
                }
            if (A[0, 0] + A[1, 1] + A[2, 2] == 0)
            {
                Form1.SetColor(0, 0, true);
                Form1.SetColor(1, 1, true);
                Form1.SetColor(2, 2, true);
                return true;
            }
            if (A[0, 2] + A[1, 1] + A[2, 0] == 0)
            {
                Form1.SetColor(0, 2, true);
                Form1.SetColor(1, 1, true);
                Form1.SetColor(2, 0, true);
                return true;
            }
            for (int i = 0; i < 3; i++)
                if (A[0, i] + A[1, i] + A[2, i] == 0)
                {
                    Form1.SetColor(0, i, true);
                    Form1.SetColor(1, i, true);
                    Form1.SetColor(2, i, true);
                    return true;
                }
            return false;
        }
        public static void firstMove()
        {
            if (A[0, 0] == 1 || A[0, 2] == 1 || A[2, 0] == 1 || A[2, 2] == 1)
            {
                A[1, 1] = 0;
                Form1.SetButton(1, 1, "O");
                count = 1;
            }
            else if (A[1, 1] == 1)
            {
                A[0, 0] = 0;
                Form1.SetButton(0, 0, "O");
                count = 2;
            }
            else if(A[0, 1] == 1 || A[1, 0] == 1)
            {
                A[0, 0] = 0;
                Form1.SetButton(0, 0, "O");
                count = 3;
            }
            else
            {
                A[2, 2] = 0;
                Form1.SetButton(2, 2, "O");
                count = 4;
            }
        }
        public static void secondMove1()
        {
            if (EnemyAttack()) { }
            else if (A[0,0] == 1)
            {
                if (A[1,2] == 1 || A[2,1] == 1)
                {
                    A[2, 2] = 0;
                    Form1.SetButton(2, 2, "O");
                }
                else
                {
                    A[2, 1] = 0;
                    Form1.SetButton(2, 1, "O");
                }
            }
            else if (A[0,2] == 1)
            {
                if (A[1, 0] == 1 || A[2, 1] == 1)
                {
                    A[2, 0] = 0;
                    Form1.SetButton(2, 0, "O");
                }
                else
                {
                    A[2, 1] = 0;
                    Form1.SetButton(2, 1, "O");
                }
            }
            else if (A[2, 0] == 1)
            {
                if (A[1, 2] == 1 || A[0, 1] == 1)
                {
                    A[0, 2] = 0;
                    Form1.SetButton(0, 2, "O");
                }
                else
                {
                    A[0, 1] = 0;
                    Form1.SetButton(0, 1, "O");
                }
            }
            else if (A[2, 2] == 1)
            {
                if (A[0, 1] == 1 || A[1, 0] == 1)
                {
                    A[0, 0] = 0;
                    Form1.SetButton(0, 0, "O");
                }
                else
                {
                    A[0, 1] = 0;
                    Form1.SetButton(0, 1, "O");
                }
            }
            count = 5;
        }
        public static void secondMove2()
        {
            if (EnemyAttack()) { }
            else if (A[2,2] == 1)
            {
                A[0, 2] = 0;
                Form1.SetButton(0, 2, "O");
            }
            count = 7;
        }
        public static void secondMove3()
        {
            if (EnemyAttack()) { }
            else if (A[0, 1] == 1)
            {
                if (A[0, 2] == 1)
                {
                    A[1, 0] = 0;
                    Form1.SetButton(1, 0, "O");
                }
                else if (A[1, 2] == 1)
                {
                    A[2, 0] = 0;
                    Form1.SetButton(2, 0, "O");
                }
                else if (A[2, 2] == 1)
                {
                    A[2, 1] = 0;
                    Form1.SetButton(2, 1, "O");
                }
                else if (A[1, 0] == 1)
                {
                    A[1, 1] = 0;
                    Form1.SetButton(1, 1, "O");
                }
                else if (A[2, 0] == 1)
                {
                    A[2, 1] = 0;
                    Form1.SetButton(2, 1, "O");
                }
            }
            else if (A[1, 0] == 1)
            {
                if (A[2, 0] == 1)
                {
                    A[0, 1] = 0;
                    Form1.SetButton(0, 1, "O");
                }
                else if (A[2, 1] == 1)
                {
                    A[0, 2] = 0;
                    Form1.SetButton(0, 2, "O");
                }
                else if (A[2, 2] == 1)
                {
                    A[1, 2] = 0;
                    Form1.SetButton(1, 2, "O");
                }
                else if (A[0, 1] == 1)
                {
                    A[1, 1] = 0;
                    Form1.SetButton(1, 1, "O");
                }
                else if (A[0, 2] == 1)
                {
                    A[1, 2] = 0;
                    Form1.SetButton(1, 2, "O");
                }
            }
            count = 7;
        }
        public static void secondMove4()
        {
            if (EnemyAttack()) { }
            else if (A[1, 2] == 1)
            {
                if (A[0, 0] == 1)
                {
                    A[1, 0] = 0;
                    Form1.SetButton(1, 0, "O");
                }
                else if (A[0, 1] == 1)
                {
                    A[2, 0] = 0;
                    Form1.SetButton(2, 0, "O");
                }
                else if (A[0, 2] == 1)
                {
                    A[2, 1] = 0;
                    Form1.SetButton(2, 1, "O");
                }
                else if (A[2, 0] == 1)
                {
                    A[1, 0] = 0;
                    Form1.SetButton(1, 0, "O");
                }
                else if (A[2, 1] == 1)
                {
                    A[1, 1] = 0;
                    Form1.SetButton(1, 1, "O");
                }
            }
            else if (A[2, 1] == 1)
            {
                if (A[0, 0] == 1)
                {
                    A[0, 1] = 0;
                    Form1.SetButton(0, 1, "O");
                }
                else if (A[1, 0] == 1)
                {
                    A[0, 2] = 0;
                    Form1.SetButton(0, 2, "O");
                }
                else if (A[2, 0] == 1)
                {
                    A[1, 2] = 0;
                    Form1.SetButton(1, 2, "O");
                }
                else if (A[0, 2] == 1)
                {
                    A[0, 1] = 0;
                    Form1.SetButton(0, 1, "O");
                }
                else if (A[1, 2] == 1)
                {
                    A[1, 1] = 0;
                    Form1.SetButton(1, 1, "O");
                }
            }
            count = 7;
        }
        public static void thirdMove1()
        {
            if (PlayerError()) { }
            else if (EnemyAttack()) { }
            else if (A[0, 0] == 1 && A[2, 0] != 1)
            {
                A[2, 0] = 0;
                Form1.SetButton(2, 0, "O");
            }
            else if (A[0, 2] == 1 && A[2, 2] != 1)
            {
                A[2, 2] = 0;
                Form1.SetButton(2, 2, "O");
            }
            else if (A[2, 0] == 1 && A[2, 2] != 1)
            {
                A[2, 2] = 0;
                Form1.SetButton(2, 2, "O");
            }
            else if (A[2, 2] == 1 && A[2, 0] != 1)
            {
                A[2, 0] = 0;
                Form1.SetButton(2, 0, "O");
            }
            else
            {
                bool flag = false;
                for (int i = 0; i < 3; i++)
                {
                    for (int j = 0; j < 3; j++)
                    {
                        if (A[i, j] == -5)
                        {
                            A[i, j] = 0;
                            Form1.SetButton(i, j, "O");
                            flag = true;
                            break;
                        }
                    }
                    if (flag) break;
                }
            }
            if (Winning())
            {
                SoundPlayer sp = new SoundPlayer(@"D:\Education\Materials of Roma Kudryk\2-ий курс\Штучний інтелект\Лаби\Lab_3_Cs\Lab_3_Cs\sound.wav");
                sp.Play();
                MessageBox.Show("You lose(");
                for (int i = 0; i < 3; i++)
                    for (int j = 0; j < 3; j++)
                    {
                        Form1.SetColor(i, j, false);
                        Form1.SetButton(i, j, "");
                        A[i, j] = -5;
                        count = 0;
                    }
            }
            else count = 8;
        }
        public static void thirdMove3()
        {
            if (PlayerError() == false)
                if (EnemyAttack() == false)
                {
                    bool flag = false;
                    for (int i = 0; i < 3; i++)
                    {
                        for (int j = 0; j < 3; j++)
                        {
                            if (A[i, j] == -5)
                            {
                                A[i, j] = 0;
                                Form1.SetButton(i, j, "O");
                                flag = true;
                                break;
                            }
                        }
                        if (flag) break;
                    }
                }
            if (Winning())
            {
                SoundPlayer sp = new SoundPlayer(@"D:\Education\Materials of Roma Kudryk\2-ий курс\Штучний інтелект\Лаби\Lab_3_Cs\Lab_3_Cs\sound.wav");
                sp.Play();
                MessageBox.Show("You lose(");
                for (int i = 0; i < 3; i++)
                    for (int j = 0; j < 3; j++)
                    {
                        Form1.SetColor(i, j, false);
                        Form1.SetButton(i, j, "");
                        A[i, j] = -5;
                        count = 0;
                    }
            }
            else count = 8;
        }
        public static void fourthMove()
        {
            if (PlayerError() == false)
                if (EnemyAttack() == false)
                {
                    bool flag = false;
                    for (int i = 0; i < 3; i++)
                    {
                        for (int j = 0; j < 3; j++)
                        {
                            if (A[i, j] == -5)
                            {
                                A[i, j] = 0;
                                Form1.SetButton(i, j, "O");
                                flag = true;
                                break;
                            }
                        }
                        if (flag) break;
                    }
                }
            if (Winning())
            {
                SoundPlayer sp = new SoundPlayer(@"D:\Education\Materials of Roma Kudryk\2-ий курс\Штучний інтелект\Лаби\Lab_3_Cs\Lab_3_Cs\sound.wav");
                sp.Play();
                MessageBox.Show("You lose(");
                for (int i = 0; i < 3; i++)
                    for (int j = 0; j < 3; j++)
                    {
                        Form1.SetColor(i, j, false);
                        Form1.SetButton(i, j, "");
                        A[i, j] = -5;
                        count = 0;
                    }
            }
            else
            {
                MessageBox.Show("Draw");
                for (int i = 0; i < 3; i++)
                    for (int j = 0; j < 3; j++)
                    {
                        Form1.SetColor(i, j, false);
                        Form1.SetButton(i, j, "");
                        A[i, j] = -5;
                        count = 0;
                    }
            }
        }
        public static void PlayerMove()
        {
            switch (ChoiceTree.count)
            {
                case 0:
                    {
                        ChoiceTree.firstMove();
                        break;
                    }
                case 1:
                    {
                        ChoiceTree.secondMove1();
                        break;
                    }
                case 2:
                    {
                        ChoiceTree.secondMove2();
                        break;
                    }
                case 3:
                    {
                        ChoiceTree.secondMove3();
                        break;
                    }
                case 4:
                    {
                        ChoiceTree.secondMove4();
                        break;
                    }
                case 5:
                    {
                        ChoiceTree.thirdMove1();
                        break;
                    }
                case 7:
                    {
                        ChoiceTree.thirdMove3();
                        break;
                    }
                default:
                    {
                        ChoiceTree.fourthMove();
                        break;
                    }
            }
        }
    }
}
