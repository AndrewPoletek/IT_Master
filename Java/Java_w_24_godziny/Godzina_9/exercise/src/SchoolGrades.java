/*
Treść zadania:
Utwórz program ktory uzywa tablicy wielowymiarowej do przechowywania ocen studentow.
Pierwszy wymiar powinien byc numerem każdego studenta, a drugi wymiar powinien byc dla ocen danego studenta.
Wyświetl średnią wszystkich ocen otrzymanych przez każdego studenta oraz ogólną średnią dla każdego z nich.
*/

class SchoolGrades{
    public static void main(String[] arguments){
        int[][] student_grades = new int[3][5];
        //First student
        student_grades[0][0] = 5;
        student_grades[0][1] = 2;
        student_grades[0][2] = 4;
        student_grades[0][3] = 6;
        //Second Student
        student_grades[1][0] = 3;
        student_grades[1][1] = 6;
        student_grades[1][2] = 1;
        student_grades[1][3] = 1;
        //Third Student
        student_grades[2][0] = 1;
        student_grades[2][1] = 1;
        student_grades[2][2] = 5;
        student_grades[2][3] = 2;

        int count_grades =0;
        int sum_grades = 0;
        for(int i=0; i<student_grades.length; i++){
            System.out.println("Student with ID: "+String.valueOf(i));
            int student_count_grades = 0;
            int student_sum_grades = 0;
            for(int g=0; g<student_grades[i].length; g++){
                sum_grades += student_grades[i][g];
                student_sum_grades +=student_grades[i][g];
                student_count_grades++;
                count_grades++;
            }
            System.out.println("Average grades for this student is: "+String.valueOf(student_sum_grades/student_count_grades));
            System.out.println();
        }
        System.out.println("Average grades for all students is:"+String.valueOf(sum_grades/count_grades));
    }
}