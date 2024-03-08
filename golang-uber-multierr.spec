# Run tests in check section
%bcond_without check

# https://github.com/uber-go/multierr
%global goipath		go.uber.org/multierr
%global forgeurl	https://github.com/uber-go/multierr
Version:		1.11.0

%gometa

Summary:	Combine one or more Go errors together
Name:		golang-uber-multierr

Release:	1
Source0:	https://github.com/uber-go/multierr/archive/v%{version}/multierr-%{version}.tar.gz
URL:		https://github.com/uber-go/multierr
License:	MIT
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildArch:	noarch

%description
Combine one or more Go errors together.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE.txt
%doc CHANGELOG.md README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n multierr-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif


