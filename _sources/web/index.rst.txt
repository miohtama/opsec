
.. This is a generated file from data/. DO NOT EDIT.

===========================================
Web development practices
===========================================

*This chapter discusses the need for web development best practices when creating sensitive Internet services.*

When developing a sensitive Internet service, special attention should be paid to the security. It is very possible to build unhackable services. Accomplishing this requires discipline and security awareness from the development team.

Most application-level vulnerabilities are related to the input handling. Any Internet facing service accepts incoming traffic and user input, both good and bad. It's a social contract: when you plug in your service to the Internet, you acknowledge that anyone in the world is allowed to use the service.

HTTP and HTML were built during an era with fewer threat models and less of a need for security. Many security features are retrofitted or they are hacked on top of the original HTML. Anyone who is not an expert in HTTP, HTML and JavaScript has a lot to learn about potential attack modes. Thus, it is an imperative that the development team uses a proper *software development framework* to build the service. Usually framework authors are well-versed in security matters and have thought out and documented the proper processes for things like form submission handling, file uploads and exposing the database to the world.




.. toctree::
    :maxdepth: 2


    https-tls-only

    database-injection

    cross-site-scripting-xss

    cross-site-request-forgery-csrf

    password-storage-best-practices

    authorization-and-permission-framework

    no-caching-policy

    non-guessable-ids

    non-public-administration-site

    whitehat-program

    code-reviews


