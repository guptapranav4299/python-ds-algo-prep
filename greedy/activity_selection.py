class ActivitySelection:
    @classmethod
    def max_activities_already_sorted(cls, start, finish):
        n = len(f)
        result = []
        i = 0
        result.append((start[0],finish[0]))
        for j in range(n):
            if start[j] >= finish[i]:
                result.append((start[j],finish[i]))
                i = j

        return result,len(result)

    @classmethod
    def max_activity_not_sorted(cls, arr, n):
        selected_activities = []
        arr.sort(key= lambda x : x[1])

        i = 0
        selected_activities.append(arr[i])

        for j in range(1, n):
            if arr[j][0] >= arr[i][1]:
                selected_activities.append(arr[j])
                i = j

        return selected_activities


if __name__ == "__main__":
    obj = ActivitySelection()
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    # activities, no_of_activities = obj.max_activities_already_sorted(s, f)
    # print("Max no of activities---->", no_of_activities)
    # print("Activities are---->", activities)

    Activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
    n = len(Activity)
    # print(obj.max_activity_not_sorted(Activity, n))
