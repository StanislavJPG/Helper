const logoutButton = document.getElementById('logOut');

if (logoutButton) {
    logoutButton.addEventListener('click', () => {
        fetch('/auth/jwt/logout', {
            method: 'POST',
        })
        .then(response => {
            if (response.ok) {
                console.log('Logout successful');
                alert('Ви успішно вийшли з профілю.')
                window.location.href = '/base';
            } else {
                console.error('Logout failed');
            }
        })
        .catch(error => {
            console.error('Error during logout:', error);
        });
    });
} else {
    console.error('Logout button not found');
}


function loginUser(email, password) {
    console.log(email);
    console.log(password);
  const loginUrl = "/auth/jwt/login";
  const loginOptions = {
    method: 'POST',
    headers: {
      'accept': 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: `grant_type=&username=${email}&password=${password}&scope=&client_id=&client_secret=`,
  };

  fetch(loginUrl, loginOptions)
    .then(response => {
      if (response.status === 422){
          document.getElementById("error-message").innerText = "Незрозумілий синтаксис"
      }
      else if (response.status === 400){
          document.getElementById("error-message").innerText = "Користувач не зареєстрований"
      }
      else
          window.location.href = '/base';
    });
}


function registerUser(email, password, username) {
    const regUrl = "/auth/register";
    const data = {
          "email": email,
          "password": password,
          "is_active": true,
          "is_superuser": false,
          "is_verified": false,
          "username": username,
          }

    const regOptions = {
        method: 'POST',
        headers: {
          'accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      };

          fetch(regUrl, regOptions)
        .then(response => {
            if (response.status === 422) {
                response.json().then(data => {
                    console.log(data);
                    document.getElementById("error-message").innerText = "Незрозумілий синтаксис";
                });
            } else if (response.status === 400) {
                document.getElementById("error-message").innerText = "Такий користувач вже зареєстрований";
            } else {
                window.location.href = '/base';
                alert('Успішна реєстрація. Підтвердіть пошту, перейшовши за посиланням.');
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}
