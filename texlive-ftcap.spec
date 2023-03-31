Name:		texlive-ftcap
Version:	17275
Release:	2
Summary:	Allows \caption at the beginning of a table-environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ftcap
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ftcap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ftcap.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
For several reasons a \caption may be desirable at the top of a
table environment. This package changes the table environment
such that \abovecaptionskip and \belowcaptionskip are swapped.
The package should also work with a non-standard table
environment.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ftcap/ftcap.sty
%doc %{_texmfdistdir}/doc/latex/ftcap/ftcap.pdf
%doc %{_texmfdistdir}/doc/latex/ftcap/ftcap.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
