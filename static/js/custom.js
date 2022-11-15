$(() => {
  let debug = true;

  // -------------------------------------------------------------------------
  // ----------------------------- [ Authentication ] ------------------------
  // -------------------------------------------------------------------------
  $("#signupForm").on("submit", async (event) => {
    event.preventDefault();
    let formData = {};
    for (let input of event.target) formData[input.name] = input.value;

    if (formData.password1 !== formData.password2) {
      alert("passwords do not match ");
      return;
    }

    const url = `${location.protocol}//${location.host}/api/register/`;

    try {
      const res = await (
        await fetch(url, {
          headers: {
            "X-CSRFToken": formData.csrfmiddlewaretoken,
          },
          body: JSON.stringify({
            first_name: formData.first_name,
            last_name: formData.last_name,
            country: formData.country,
            phone: formData.phone,
            email: formData.email,
            zipcode: formData.zipcode,
            password1: formData.password1,
            password2: formData.password2,
            account_category: formData.account_category
          }),
          method: "POST",
        })
      ).json();

      console.log("🚀 ~ file: custom.js ~ line 20 ~ $ ~ res", res);
    } catch (err) {
      console.log("🚀 ~ file: custom.js ~ line 26 ~ $ ~ err", err);
    }
  });



  // --------------------------------------
  // -------------- Login -----------------
  // --------------------------------------
  $("#loginForm").on("submit", async (event) => {
    event.preventDefault();
    let formData = {};
    for (let input of event.target) formData[input.name] = input.value;

    if (debug) console.log("🚀 ~ file: custom.js ~ line 8 ~ $ ~ formData", formData);

    // localhost:8000 || shouuts/api/register/
    const url = `${location.protocol}//${location.host}/api/login/`;

    try {
      const res = await (
        await fetch(url, {
          headers: {
            "X-CSRFToken": formData.csrfmiddlewaretoken,
          },
          body: JSON.stringify({
            email: formData.email,
            password: formData.password,
          }),
          method: "POST",
        })
      ).json();

      console.log("🚀 ~ file: custom.js ~ line 20 ~ $ ~ res", res);
    } catch (err) {
      console.log("🚀 ~ file: custom.js ~ line 26 ~ $ ~ err", err);
    }
  })

});
