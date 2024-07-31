(function () {
  "use strict";

  let forms = document.querySelectorAll('.php-email-form');

  forms.forEach(function(e) {
    e.addEventListener('submit', function(event) {
      event.preventDefault();

      let thisForm = this;

      let action = thisForm.getAttribute('action');
      let recaptcha = thisForm.getAttribute('data-recaptcha-site-key');
      
      if (!action) {
        displayError(thisForm, 'The form action property is not set!');
        return;
      }
      thisForm.querySelector('.loading').classList.add('d-block');
      thisForm.querySelector('.error-message').classList.remove('d-block');
      thisForm.querySelector('.sent-message').classList.remove('d-block');

      let formData = new FormData(thisForm);

      let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
      formData.append('csrfmiddlewaretoken', csrftoken);

      if (recaptcha) {
        if (typeof grecaptcha !== "undefined") {
          grecaptcha.ready(function() {
            try {
              grecaptcha.execute(recaptcha, { action: 'php_email_form_submit' })
                .then(token => {
                  formData.set('recaptcha-response', token);
                  php_email_form_submit(thisForm, action, formData);
                })
            } catch (error) {
              displayError(thisForm, error);
            }
          });
        } else {
          displayError(thisForm, 'The reCaptcha javascript API url is not loaded!')
        }
      } else {
        php_email_form_submit(thisForm, action, formData);
      }
    });
  });

  function php_email_form_submit(thisForm, action, formData) {
    let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch(action, {
      method: 'POST',
      body: formData,
      headers: {
        'X-Requested-With': 'XMLHttpRequest',
        'X-CSRFToken': csrftoken
      }
    })
    .then(response => response.json().then(data => {
      if (response.ok) {
        return data;
      } else {
        throw new Error(data.message || `${response.url} ${response.status} ${response.statusText}`);
      }
    }))
    .then(data => {
      thisForm.querySelector('.loading').classList.remove('d-block');
      if (data.error === 'false') {
        thisForm.querySelector('.sent-message').classList.add('d-block');
        thisForm.querySelector('.sent-message').innerHTML = data.message;
        thisForm.reset();
        setTimeout(() => {
          window.location.reload();
        }, 2000);
      } else if (data.error === 'true') {
        displayError(thisForm, data.message);
      } else {
        throw new Error(data ? data : 'Form submission failed and no error message returned from: ' + action);
      }
    })
    .catch((error) => {
      displayError(thisForm, error);
    });
  }

  function displayError(thisForm, error) {
    thisForm.querySelector('.loading').classList.remove('d-block');
    thisForm.querySelector('.error-message').innerHTML = error;
    thisForm.querySelector('.error-message').classList.add('d-block');
  }

})();
