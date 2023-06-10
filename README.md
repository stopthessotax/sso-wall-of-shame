# SSO Wall of Shame

## Intro

Single sign-on (SSO) is a mechanism for outsourcing the authentication for your website (or other product) to a third party identity provider, such as Google, Azure AD, Okta, PingFederate, etc.

In this context, SSO refers to a SaaS or similar vendor allowing a business client to manage user accounts via the client’s own identity provider, without having to rely on the vendor to provide strong authentication with audit logs, and with the ability to create and delete user accounts centrally, for all users, across all software in use by that client.

For organizations with more than a handful of employees, this feature is critical for IT and Security teams to be able to effectively manage user accounts across dozens or hundreds of vendors, many of which don’t support features like TOTP 2FA or U2F. In the event that an employee leaves the company, it allows the IT team to immediately disable their access to all applications, rather than logging into 100 different user management portals.

In short: SSO is a core security requirement for any company with more than five employees.

SaaS vendors appear not to have received this message, however. SSO is often only available as part of “Enterprise” pricing, which assumes either a huge number of users (minimum seat count) or is force-bundled with other “Enterprise” features which may have no value to the company using the software.

If companies claim to “take your security seriously”, then SSO should be available as a feature that is either:

    part of the core product, or
    an optional paid extra for a reasonable delta, or
    attached to a price tier, but with a reasonably small gap between the non-SSO tier and SSO tiers.

Many vendors charge 2x, 3x, or 4x the base product pricing for access to SSO, which disincentivizes its use and encourages poor security practices.

## Contributing

If you'd like to add a SaaS vendor to the list who charges for SSO functionality, or (even better!) remove a vendor who remove the SSO tax, please open a pull request!  Alternatively, you can open a new GitHub ticket for this repository and fill out the associated form and a maintainer will submit the pull request on your behalf.

# Acknowledgements

This is a fork of the original [robchahin/sso-wall-of-shame](https://github.com/robchahin/sso-wall-of-shame) which was published at https://sso.tax. We thanks Rob for his idea and work in starting the project, and we were sad to see the original repository go dormant. We believe this is continues to a valuable effort and thus this fork was created and we welcome all contributions!
