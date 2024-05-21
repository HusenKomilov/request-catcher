from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(
        "sub",
        "domain.urls",
        name="domain"
        )
)