class Report:

    def generate_report(self,data):
        
        lines=[]
        lines.append("your report of this week")

        winner= data.get("most common")

        if winner:
            lines.append(f"your top emotion of this week {winner[0]} ")


        return "/n".join(lines)
