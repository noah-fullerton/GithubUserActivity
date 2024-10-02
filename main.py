import typer
import requests

app = typer.Typer()

def main(username: str):
    pass

def get_events(username: str):
    response = requests.get(f"https://api.github.com/users/{username}/events")
    events = response.json()
    return events

def format_events(events):
    formattedEvents = []
    for event in events:
        formattedEvents.append(f"{eventToString(event['type'])} {event['repo']['name']}")
    return formattedEvents

def eventToString(event):
    switcher = {
        "PushEvent": "Pushed to",
        "CreateEvent": "Created",
        "DeleteEvent": "Deleted",
        "ForkEvent": "Forked",
        "PullRequestEvent": "Opened a pull request in",
        "IssuesEvent": "Opened an issue in",
        "IssueCommentEvent": "Commented on an issue in",
        "WatchEvent": "Starred",
        "ReleaseEvent": "Released"
    }
    return switcher.get(event, "Invalid event")

def print_events(events):
    for event in events:
        print(event)

if __name__ == "__main__":
    print_events(format_events(get_events("noah-fullerton")))
    #typer.run(main)