"""
n = len(courses)
finish the course with tighter deadline sooner? Is it optimal?

taken 0

sort by deadline

currentTotalTime

max heap: course duration, course starttime

swap: 

"""
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # sort by end day
        courses.sort(key=lambda x:x[1])
        time = 0 # current time
        count = 0
        for i in range(len(courses)):
            if time + courses[i][0] <= courses[i][1]:
                # able to meet the deadline
                time += courses[i][0]
                courses[count][0], courses[count][1] = courses[i][0],courses[i][1]
                count += 1
            else:
                # try to find a candidate class for swapping
                max_i = i
                for j in range(count):
                    if courses[j][0] > courses[max_i][0]:
                        max_i = j
                if courses[max_i][0] > courses[i][0]:
                    # found a course other than itself, swap in
                    # duration_i < duration_j, the current course can surely take its place.
                    time = time - courses[max_i][0] + courses[i][0]
                    courses[max_i][0], courses[max_i][1] = courses[i][0],courses[i][1]
        return count
        
        
