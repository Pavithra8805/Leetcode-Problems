class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int totalTank = 0;
        int currentTank = 0;
        int startIndex = 0;

        for (int i = 0; i < gas.size(); ++i) {
            int net = gas[i] - cost[i];
            totalTank += net;
            currentTank += net;

            // If we run out of fuel, station i cannot be reached from startIndex.
            // None of the stations between startIndex and i can be the start either.
            if (currentTank < 0) {
                startIndex = i + 1;
                currentTank = 0;
            }
        }

        // If the total gas is less than the total cost, completing the circuit is impossible.
        return totalTank >= 0 ? startIndex : -1;
    }
};