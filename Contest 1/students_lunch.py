class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        c = 0
        while len(students) > c:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                c = 0
            else:
                students.append(students[0])
                c+=1

            students.pop(0)
        return len(students)