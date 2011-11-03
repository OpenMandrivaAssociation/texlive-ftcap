# revision 17275
# category Package
# catalog-ctan /macros/latex/contrib/ftcap
# catalog-date 2010-03-09 13:05:51 +0100
# catalog-license gpl
# catalog-version 1.4
Name:		texlive-ftcap
Version:	1.4
Release:	1
Summary:	Allows \caption at the beginning of a table-environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ftcap
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ftcap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ftcap.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
For several reasons a \caption may be desirable at the top of a
table environment. This package changes the table environment
such that \abovecaptionskip and \belowcaptionskip are swapped.
The package should also work with a non-standard table
environment.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ftcap/ftcap.sty
%doc %{_texmfdistdir}/doc/latex/ftcap/ftcap.pdf
%doc %{_texmfdistdir}/doc/latex/ftcap/ftcap.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
