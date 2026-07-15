"""import smtplib


my_email = "kerreyabba@gmail.com"


password = "13261y7172yy2y222v"

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()

        connection.login(my_email, password)

        subject = "Test"
        body = "Bonjour ! Ceci est un email envoyé avec Python."

        message = f"Subject: {subject}\n\n{body}"

        connection.sendmail(
            from_addr=my_email,
            to_addrs="@gmail.com",
            msg=message
        )

    print("Email envoyé avec succès !")

except smtplib.SMTPAuthenticationError:
    print("Erreur : authentification échouée.")
    print("Vérifiez votre adresse Gmail et utilisez un mot de passe d'application Google.")
except Exception as e:
    print("Une erreur est survenue :", e)


    """

import datetime as dt

now=dt.datetime.now()
year=now.year
month=now.month
date_of_week=now.weekday()
#print(date_of_week)
print(now)