import threading
import resend
from decouple import config
resend.api_key = config("RESEND")


def send_email_async(email_data):
    # Send the email using the resend module
    resend.Emails.send(email_data)

def booking_confirmed_email(email, name ):
                # Define the email data
    email_data = {
        "from": "Moses.cam <noreply@moses.cam>",
        "to": email,
        "subject": "Booking Confirmed! Can't Wait to Capture Your Moments!",
        "html": f"""
            <!DOCTYPE html>
            <html lang="en">
            
            <body style="background: #F9F6F1;">
                <div class="container" >
                    <td align="center" valign="top" bgcolor="#ffffff" style="border-radius:5px;border-left:1px solid #e0bce7;border-top:1px solid #e0bce7;border-right:1px solid #efefef;border-bottom:1px solid #efefef">
                    <table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0">
                        <tbody>
                    
                        

                        
                        <tr>
                            <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:16px; font-weight: 600;line-height:24px;color:#414347;padding:40px 40px 20px 40px">
                                Hi, {name} 
                            </td>
                        </tr>
                       
                        <tr>
                            <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px;line-height:24px;color:#414347;padding:40px 40px 20px 40px">
                            Thank you for reaching out to me! I am excited to work with you.</td>
                        </tr>


                        
                        <tr>
                            <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px;line-height:24px;color:#414347;padding:20px 40px 20px 40px">
                                In order to move forward, i just need the following.<br>
                                <span  style=" font-weight: 600;">1. Timeline</span> <br>
                                <span  style=" font-weight: 600;">2. Full Brief</span> <br>
                                <span  style="font-weight: 600;">3. Project Budget</span> <br>
                            </td>
                        </tr>
                        
                        
                        <tr>
                            <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px;line-height:24px;padding:20px 20px 0px 40px">
                                How about we set a call for further details?
                                
                            </td>
                        </tr>

                        <tr>
                            <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px;line-height:24px;padding:40px 20px 0px 40px">
                                For your convenience, please do not reply to this email. For any direct inquiries or assistance, feel free to reach me personally at <br>
                                <a href="mailto:Moschimereze@gmail.com" style="text-decoration: none; font-weight: 600; color: #333333;">Moschimereze@gmail.com</a>
                        </tr>

                        
                        </tbody>
                    </table>
                    </td>
                </div>
            </body>
            </html>
        """,
    }

    # Create a thread to send the email asynchronously
    email_thread = threading.Thread(target=send_email_async, args=(email_data,))
    email_thread.start()
    
def alert_owner(email, name, category,  phone_number, additional_details, heard_about_us):
                # Define the email data
    email_data = {
        "from": "Moses.cam <noreply@moses.cam>",
        "to": "Moschimereze@gmail.com",
        "subject": "New Client!",
        "html": f"""
           <!DOCTYPE html>
            <html lang="en">
            
            <body style="background: #F9F6F1;">
                <div class="container" >
                    <td align="center" valign="top" bgcolor="#ffffff" style="border-radius:5px;border-left:1px solid #e0bce7;border-top:1px solid #e0bce7;border-right:1px solid #efefef;border-bottom:1px solid #efefef">
                    <table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0">
                        <tbody>
                    
                        

                        
                        <tr>
                            <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:16px; font-weight: 600;line-height:24px;color:#414347;padding:40px 40px 20px 40px">
                                Hello Moses, you have received a booking from a potential client
                            </td>
                        </tr>
                       
                        <tr>
                            <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px; font-weight: 600;line-height:24px;color:#414347;padding:40px 40px 20px 40px">
                            Check out what they submitted.</td>
                        </tr>


                        
                        <tr>
                            <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px;line-height:24px;color:#414347;padding:20px 40px 20px 40px">
                                <ul style="list-style-type: none; padding: 0; margin: 0;">
                                    <li style="padding: 10px 0; border-bottom: 1px solid #dddddd;">
                                        <strong style="color: #333333;">Name:</strong> <span style="color: #555555;">{name}</span>
                                    </li>
                                    <li style="padding: 10px 0; border-bottom: 1px solid #dddddd;">
                                        <strong style="color: #333333;">Email:</strong> <span style="color: #555555;">{email}</span>
                                    </li>
                                    <li style="padding: 10px 0; border-bottom: 1px solid #dddddd;">
                                        <strong style="color: #333333;">Phone number:</strong> <span style="color: #555555;">{phone_number}</span>
                                    </li>
                                    <li style="padding: 10px 0; border-bottom: 1px solid #dddddd;">
                                        <strong style="color: #333333;">Category chosen:</strong> <span style="color: #555555;">{category}</span>
                                    </li>
                                    <li style="padding: 10px 0; border-bottom: 1px solid #dddddd;">
                                        <strong style="color: #333333;">Additional details:</strong> <span style="color: #555555;">{additional_details}</span>
                                    </li>
                                    <li style="padding: 10px 0; border-bottom: 1px solid #dddddd;">
                                        <strong style="color: #333333;">Heard about you from:</strong> <span style="color: #555555;">{heard_about_us}</span>
                                    </li>
                                </ul>
                            </td>
                        </tr>
                        
                        
                        

                        
                        </tbody>
                    </table>
                    </td>
                </div>
            </body>
            </html>
        """,
    }

    # Create a thread to send the email asynchronously
    email_thread = threading.Thread(target=send_email_async, args=(email_data,))
    email_thread.start()