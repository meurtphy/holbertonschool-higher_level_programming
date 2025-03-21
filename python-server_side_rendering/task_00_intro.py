import os

def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if template is empty
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with attendee data, using "N/A" for missing values
        invitation = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # Generate output file name
        output_filename = f"output_{index}.txt"

        # Write the invitation to the output file
        with open(output_filename, "w") as output_file:
            output_file.write(invitation)

        print(f"Generated: {output_filename}")