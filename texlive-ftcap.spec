%global tl_name ftcap
%global tl_revision 17275

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Allows \caption at the beginning of a table-environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ftcap
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ftcap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ftcap.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
For several reasons a \caption may be desirable at the top of a table
environment. This package changes the table environment such that
\abovecaptionskip and \belowcaptionskip are swapped. The package should
also work with a non-standard table environment.

