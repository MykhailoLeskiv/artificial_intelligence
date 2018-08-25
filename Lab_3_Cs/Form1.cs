using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lab_3_Cs
{
    public partial class Form1 : Form
    {
        public static Button[,] btns = new Button[3, 3];
        public static void SetButton(int x, int y, string text) => btns[x, y].Text = text;
        public static void SetColor(int x, int y, bool flag)
        {
            if(flag)
                btns[x, y].ForeColor = Color.Red;
            else btns[x, y].ForeColor = Color.Black;
        }

        public Form1()
        {
            InitializeComponent();
            btns[0, 0] = button00;
            btns[0, 1] = button01;
            btns[0, 2] = button02;
            btns[1, 0] = button10;
            btns[1, 1] = button11;
            btns[1, 2] = button12;
            btns[2, 0] = button20;
            btns[2, 1] = button21;
            btns[2, 2] = button22;
            ChoiceTree tut = new ChoiceTree();
        }
        private void button00_Click(object sender, EventArgs e)
        {
            if (btns[0, 0].Text == "")
            {
                btns[0, 0].Text = "X";
                ChoiceTree.A[0, 0] = 1;
                ChoiceTree.PlayerMove();
            }
        }
        private void button01_Click(object sender, EventArgs e)
        {
            if (btns[0, 1].Text == "")
            {
                btns[0, 1].Text = "X";
                ChoiceTree.A[0, 1] = 1;
                ChoiceTree.PlayerMove();
            }
        }

        private void button02_Click(object sender, EventArgs e)
        {
            if (btns[0, 2].Text == "")
            {
                btns[0, 2].Text = "X";
                ChoiceTree.A[0, 2] = 1;
                ChoiceTree.PlayerMove();
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            if (btns[1, 0].Text == "")
            {
                btns[1, 0].Text = "X";
                ChoiceTree.A[1, 0] = 1;
                ChoiceTree.PlayerMove();
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            if (btns[1, 1].Text == "")
            {
                btns[1, 1].Text = "X";
                ChoiceTree.A[1, 1] = 1;
                ChoiceTree.PlayerMove();
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            if (btns[1, 2].Text == "")
            {
                btns[1, 2].Text = "X";
                ChoiceTree.A[1, 2] = 1;
                ChoiceTree.PlayerMove();
            }
        }

        private void button20_Click(object sender, EventArgs e)
        {
            if (btns[2, 0].Text == "")
            {
                btns[2, 0].Text = "X";
                ChoiceTree.A[2, 0] = 1;
                ChoiceTree.PlayerMove();
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            if (btns[2, 1].Text == "")
            {
                btns[2, 1].Text = "X";
                ChoiceTree.A[2, 1] = 1;
                ChoiceTree.PlayerMove();
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
            if (btns[2, 2].Text == "")
            {
                btns[2, 2].Text = "X";
                ChoiceTree.A[2, 2] = 1;
                ChoiceTree.PlayerMove();
            }
        }
    }
}
