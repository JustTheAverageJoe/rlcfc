import updatetopscorers
import league_table_generator
import updateinjuries
from datetime import datetime
from datetime import timezone

if __name__ == '__main__':
    current_time = datetime.now(timezone.utc)
    timestamp = current_time.strftime("^Last ^updated ^at ^%H:%M:%S-%d-%b-%Y")
    print("\n")
    print("updating top scorers")
    updatetopscorers.topscorers(timestamp)
    print("updating league table")
    league_table_generator.GetLeagueTableData(timestamp)
    print("updating injuries")
    updateinjuries.injuries(timestamp)
