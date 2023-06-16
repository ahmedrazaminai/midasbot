function waitForElement(selector) {
	const findElement = sel =>
		new Promise(resolve => {
			if (document.querySelector(sel)) {
				return resolve(document.querySelector(sel));
			}

			const observer = new MutationObserver(_ => {
				if (document.querySelector(sel)) {
					resolve(document.querySelector(sel));
					observer.disconnect();
				}
			});

			observer.observe(document.body, {
				childList: true,
				subtree: true,
			});
		});

	const timeout = new Promise((_, reject) =>
		setTimeout(() => reject(`Timed out after ${milliseconds} ms.`), milliseconds)
	);

	return Promise.race([findElement(selector), timeout]);
}

