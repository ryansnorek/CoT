# --------------------------------------------------------------------------------
# Prompt user to select parameters for analysis on current CoT report
# --------------------------------------------------------------------------------

def getMinimumPercentFilter():

    def prompt():
        minimumPercentFilter = int(
            input("Select a minimum percent change filter for CoT report: "))

        if (minimumPercentFilter < 0):
            getMinimumPercentFilter()

        return minimumPercentFilter

    return prompt()
